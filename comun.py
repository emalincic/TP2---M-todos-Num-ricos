"""Carga compartida de los datos del TP2 (composición de espectros estelares).

``cargar_datos()`` lee los cuatro archivos CSV de la carpeta ``Archivos/`` y
devuelve un diccionario con:

- ``lam``: longitudes de onda λ [Å], forma (4300,).
- ``A``: matriz de espectros SSP, forma (4300, 15). La columna j es el espectro
  de una población de edad ``edades[j]``.
- ``edades``: edades de las SSP [Gyr], forma (15,), leídas de los nombres de columna.
- ``b``: espectro medido con ruido, forma (4300,).
- ``b_ideal``: espectro ideal sin ruido, forma (4300,).
- ``x_real``: composición real (proporciones que suman 1), forma (15,).
"""

from pathlib import Path

import numpy as np
import pandas as pd

CARPETA_DATOS = Path(__file__).resolve().parent / "Archivos"


def cargar_datos():
    """Lee los datos del TP2, verifica su consistencia y los devuelve.

    Returns:
        dict: diccionario con las claves ``lam``, ``A``, ``edades``, ``b``,
        ``b_ideal`` y ``x_real`` (ver la documentación del módulo).

    Raises:
        AssertionError: si la forma de ``A`` no es (4300, 15), si las longitudes
            de onda de los tres archivos no coinciden, si ``x_real`` no suma 1
            o si las edades de las columnas no coinciden con ``edad_Gyr``.
    """
    df_A = pd.read_csv(CARPETA_DATOS / "longitudondayA.csv")
    df_ruido = pd.read_csv(CARPETA_DATOS / "espectro_ruido.csv")
    df_ideal = pd.read_csv(CARPETA_DATOS / "espectroideal.csv")
    df_x = pd.read_csv(CARPETA_DATOS / "x_real.csv")

    # Matriz A: la primera columna es λ y el resto son los espectros SSP.
    lam = df_A["longitud_onda_A"].to_numpy(dtype=float)
    columnas_ssp = [c for c in df_A.columns if c != "longitud_onda_A"]
    A = df_A[columnas_ssp].to_numpy(dtype=float)
    # La edad de cada SSP está codificada en el nombre de la columna: SSP_<edad>_Gyr.
    edades = np.array([float(c.split("_")[1]) for c in columnas_ssp])

    lam_ruido = df_ruido["longitud_onda_A"].to_numpy(dtype=float)
    b = df_ruido["flujo_b_con_ruido"].to_numpy(dtype=float)

    lam_ideal = df_ideal["longitud_onda_A"].to_numpy(dtype=float)
    b_ideal = df_ideal["flujo_b_ideal"].to_numpy(dtype=float)

    edades_x = df_x["edad_Gyr"].to_numpy(dtype=float)
    x_real = df_x["proporcion_x_real"].to_numpy(dtype=float)

    assert A.shape == (4300, 15), f"A tiene forma {A.shape}, se esperaba (4300, 15)"
    assert np.array_equal(lam, lam_ruido), "Las λ de espectro_ruido.csv no coinciden con las de A"
    assert np.array_equal(lam, lam_ideal), "Las λ de espectroideal.csv no coinciden con las de A"
    assert np.isclose(x_real.sum(), 1), f"x_real suma {x_real.sum()}, se esperaba 1"
    assert np.allclose(edades, edades_x, rtol=1e-2), (
        "Las edades de las columnas de A no coinciden con edad_Gyr de x_real.csv"
    )

    return {
        "lam": lam,
        "A": A,
        "edades": edades,
        "b": b,
        "b_ideal": b_ideal,
        "x_real": x_real,
    }
