# Herramientas — `tools/`

Utilidades auxiliares del curso **Simulación de Riesgos y Coberturas (SimRC)**.

## `author_lookup.py` — Filtrado de autores por impacto de citas

Busca autores en la base de datos **«Updated science-wide author databases of
standardized citation indicators»** (Ioannidis, Boyack & Baas, 2020), tabla de
carrera completa `Table_1_Authors_career_2024.xlsx`.

Generaliza el filtro original de pandas añadiendo:

- **Búsqueda insensible a acentos, mayúsculas y separadores.** «Sanchez Torres»
  encuentra «Sánchez-Torres» sin escribir variantes con `regex`.
- **Alternativas** separadas por `|` (p. ej. `"Sanchez Torres|Ioannidis"`).
- **Resolución flexible de columnas**: los encabezados cambian entre cosechas
  anuales (`c-score (ns)`, `rank (ns)`, …); las que no existen se omiten.
- **CLI** y exportación opcional a CSV.

### Obtener los datos

El archivo `.xlsx` es grande (~varios cientos de MB) y **no** se versiona en
este repositorio. Descárgalo del repositorio de datos de Elsevier y colócalo
junto al script:

> https://elsevier.digitalcommonsdata.com/datasets/btchxktzyw

### Uso

```bash
# Búsqueda básica (subconjunto de columnas curado)
python tools/author_lookup.py "Sanchez Torres"

# Indicar la ruta del archivo
python tools/author_lookup.py "Sanchez Torres" --file Table_1_Authors_career_2024.xlsx

# Varias personas a la vez y exportar a CSV
python tools/author_lookup.py "Sanchez Torres|Ioannidis" --csv resultado.csv

# Todas las columnas del dataset
python tools/author_lookup.py "Ioannidis" --all-columns
```

### Uso como módulo

```python
from tools.author_lookup import lookup, find_authors, load_table

df = load_table("Table_1_Authors_career_2024.xlsx")
hits = find_authors(df, "Sanchez Torres")   # filas completas
curado = lookup("Sanchez Torres")           # solo columnas de interés
```

### Columnas mostradas por defecto

| Columna         | Significado                                            |
|-----------------|--------------------------------------------------------|
| `authfull`      | Nombre completo del autor                              |
| `inst_name`     | Institución                                            |
| `cntry`         | País (código ISO)                                      |
| `np6024`        | Número de artículos (1960–2024)                        |
| `h24`           | Índice *h* (a 2024)                                    |
| `c-score (ns)`  | *Composite score* (excluyendo autocitas, *ns*)        |
| `rank (ns)`     | Posición global por *composite score* (*ns*)          |
| `sm-subfield-1` | Subcampo científico principal                          |

### Referencia

Ioannidis, J. P. A., Boyack, K. W. & Baas, J. (2020). Updated science-wide
author databases of standardized citation indicators. *PLOS Biology*, 18(10),
e3000918.
