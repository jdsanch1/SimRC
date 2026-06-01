"""
author_lookup.py — Filtrado de autores en la base de datos de impacto de citas.

Curso: Simulación de Riesgos y Coberturas (SimRC)
Profesor: Juan Diego Sánchez Torres — MAF ITESO

Herramienta reutilizable para buscar autores en la base de datos
«Updated science-wide author databases of standardized citation indicators»
(Ioannidis et al., Elsevier Data Repository / PLOS Biology), versión de
carrera completa (career-long), tabla `Table_1_Authors_career_2024.xlsx`.

Generaliza el snippet original:

    import pandas as pd
    df = pd.read_excel("Table_1_Authors_career_2024.xlsx")
    mask = df["authfull"].str.contains(
        "Sánchez-Torres|Sanchez Torres", case=False, na=False, regex=True)
    df.loc[mask, ["authfull", "inst_name", "cntry", "np6024",
                  "h24", "c-score (ns)", "rank (ns)", "sm-subfield-1"]]

añadiendo:
  - Normalización de acentos y signos de puntuación, de modo que
    «Sanchez Torres» encuentre «Sánchez-Torres» sin escribir variantes.
  - Selección tolerante de columnas (los nombres varían entre cosechas
    anuales del dataset: c-score / 'composite score', rank, etc.).
  - Interfaz de línea de comandos y exportación opcional a CSV.

Referencias:
  - Ioannidis, J. P. A., Boyack, K. W. & Baas, J. (2020). Updated
    science-wide author databases of standardized citation indicators.
    PLOS Biology, 18(10), e3000918.

Uso:
    python author_lookup.py "Sanchez Torres"
    python author_lookup.py "Sanchez Torres" --file Table_1_Authors_career_2024.xlsx
    python author_lookup.py "Ioannidis" --csv resultado.csv
"""

from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path

import pandas as pd

# Nombre por defecto de la tabla career-long (cosecha 2024).
DEFAULT_FILE = "Table_1_Authors_career_2024.xlsx"

# Columna con el nombre completo del autor en el dataset.
NAME_COLUMN = "authfull"

# Columnas que se desean mostrar, en orden de preferencia. Los nombres
# exactos cambian entre versiones anuales, por lo que `select_columns`
# resuelve cada una de forma flexible (sin acentos, sin mayúsculas,
# ignorando espacios/guiones).
PREFERRED_COLUMNS = [
    "authfull",
    "inst_name",
    "cntry",
    "np6024",
    "h24",
    "c-score (ns)",
    "rank (ns)",
    "sm-subfield-1",
]


def strip_accents(text: str) -> str:
    """Elimina acentos/diacríticos de una cadena (NFKD)."""
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def normalize(text: str) -> str:
    """Normaliza para comparación: minúsculas, sin acentos y sin separadores.

    Convierte guiones, espacios y puntuación en un único espacio, de modo
    que «Sánchez-Torres», «Sanchez Torres» y «sanchez  torres» coincidan.
    """
    text = strip_accents(str(text)).lower()
    cleaned = []
    for ch in text:
        cleaned.append(ch if ch.isalnum() else " ")
    return " ".join("".join(cleaned).split())


def load_table(path: Path) -> pd.DataFrame:
    """Carga la tabla de autores desde Excel o CSV.

    Parameters
    ----------
    path : Path
        Ruta al archivo `.xlsx` (o `.csv`) descargado del repositorio de datos.

    Returns
    -------
    pd.DataFrame
    """
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró '{path}'.\n"
            "Descarga la tabla career-long desde el repositorio de datos de "
            "Elsevier (Ioannidis et al.):\n"
            "  https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw\n"
            f"y colócala junto a este script como '{DEFAULT_FILE}'."
        )
    if path.suffix.lower() in {".csv", ".txt"}:
        return pd.read_csv(path)
    return pd.read_excel(path)


def select_columns(df: pd.DataFrame, preferred=PREFERRED_COLUMNS) -> list[str]:
    """Resuelve `preferred` contra las columnas reales del DataFrame.

    La coincidencia es flexible (sin acentos/mayúsculas/separadores), pues los
    encabezados cambian entre cosechas anuales del dataset. Las columnas que no
    se encuentren se omiten silenciosamente.
    """
    lookup = {normalize(col): col for col in df.columns}
    resolved = []
    for want in preferred:
        actual = lookup.get(normalize(want))
        if actual is not None and actual not in resolved:
            resolved.append(actual)
    return resolved


def find_authors(
    df: pd.DataFrame,
    query: str,
    name_column: str = NAME_COLUMN,
) -> pd.DataFrame:
    """Devuelve las filas cuyo nombre de autor coincide con `query`.

    La búsqueda es insensible a acentos, mayúsculas y separadores. Se aceptan
    varias alternativas separadas por «|» (p. ej. «Sanchez Torres|Smith»).

    Parameters
    ----------
    df : pd.DataFrame
        Tabla de autores.
    query : str
        Texto a buscar (subcadena normalizada). Admite alternativas con «|».
    name_column : str
        Columna que contiene el nombre completo del autor.

    Returns
    -------
    pd.DataFrame
        Subconjunto de `df` con las filas coincidentes.
    """
    if name_column not in df.columns:
        raise KeyError(
            f"La columna '{name_column}' no está en el archivo. "
            f"Columnas disponibles: {list(df.columns)}"
        )

    terms = [normalize(part) for part in query.split("|") if part.strip()]
    if not terms:
        return df.iloc[0:0]

    normalized_names = df[name_column].map(normalize)
    mask = pd.Series(False, index=df.index)
    for term in terms:
        mask |= normalized_names.str.contains(term, regex=False, na=False)
    return df.loc[mask]


def lookup(
    query: str,
    file: str | Path = DEFAULT_FILE,
    columns=PREFERRED_COLUMNS,
) -> pd.DataFrame:
    """Carga la tabla, busca `query` y devuelve solo las columnas deseadas."""
    df = load_table(Path(file))
    hits = find_authors(df, query)
    cols = select_columns(hits, columns)
    return hits[cols] if cols else hits


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Busca autores en la base de datos de impacto de citas "
            "(Ioannidis et al., career-long)."
        )
    )
    parser.add_argument(
        "query",
        help="Nombre a buscar (acepta alternativas con '|'). "
        "Insensible a acentos, mayúsculas y guiones.",
    )
    parser.add_argument(
        "--file",
        "-f",
        default=DEFAULT_FILE,
        help=f"Ruta a la tabla de autores (por defecto: {DEFAULT_FILE}).",
    )
    parser.add_argument(
        "--csv",
        help="Ruta opcional para exportar las coincidencias a CSV.",
    )
    parser.add_argument(
        "--all-columns",
        action="store_true",
        help="Muestra todas las columnas en lugar del subconjunto curado.",
    )
    return parser


def main(argv=None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        df = load_table(Path(args.file))
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        hits = find_authors(df, args.query)
    except KeyError as exc:
        print(exc, file=sys.stderr)
        return 1

    if not args.all_columns:
        cols = select_columns(hits)
        if cols:
            hits = hits[cols]

    if hits.empty:
        print(f"Sin coincidencias para «{args.query}».")
        return 0

    # Evita truncar columnas en la salida de consola.
    with pd.option_context(
        "display.max_columns", None,
        "display.width", None,
        "display.max_colwidth", 60,
    ):
        print(hits.to_string(index=False))

    print(f"\n{len(hits)} coincidencia(s).")

    if args.csv:
        hits.to_csv(args.csv, index=False)
        print(f"Resultados guardados en '{args.csv}'.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
