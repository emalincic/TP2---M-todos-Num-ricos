# TP2 — Composición de espectros estelares (SVD y cuadrados mínimos)

Métodos Numéricos y Optimización · UdeSA · 2º sem. 2026 · Entrega: 18/11/2026 23:59.

## Estructura
- `TP2_completo.ipynb` — **versión de entrega**: los cinco ejercicios en un solo notebook, pensado para Colab. No depende de `comun.py` ni guarda figuras.
- `consigna_tp2.pdf` — enunciado.
- `Archivos/` — datos (A con λ en la 1ª columna, b con ruido, b ideal, x real).
- `comun.py` — carga de datos compartida (`cargar_datos()`) para los notebooks por ejercicio.
- `Ej1_Exploracion/` … `Ej5_Espectros_Indistinguibles/` — un notebook por ejercicio, con sus figuras en `figuras/`.

## Cómo correr
- `TP2_completo.ipynb`: ejecutarlo de arriba a abajo. Busca los CSV en `Archivos/` y, si no están (por ejemplo en Colab), los descarga de este repositorio.
- Notebooks por ejercicio: abrir el de cada carpeta; importa `comun.py` desde la carpeta padre.
