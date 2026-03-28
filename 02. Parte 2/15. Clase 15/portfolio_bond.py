"""
portfolio_bond.py — Alias de portfolio_func.py para compatibilidad.

Todas las funciones (incluyendo optimal_portfolio_b para portafolios
con bono) están definidas en portfolio_func.py. Este módulo las
re-exporta para mantener compatibilidad con notebooks anteriores.

Curso: Simulación de Riesgos y Coberturas (SimRC)
Profesor: Juan Diego Sánchez Torres — MAF ITESO
"""

from portfolio_func import (
    get_historical_closes,
    calc_daily_returns,
    sim_mont_portfolio,
    optimal_portfolio,
    optimal_portfolio_b,
)

__all__ = [
    "get_historical_closes",
    "calc_daily_returns",
    "sim_mont_portfolio",
    "optimal_portfolio",
    "optimal_portfolio_b",
]
