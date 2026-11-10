# Ejercicio 4 — Regularización de Tikhonov

Explore en qué consiste la regularización de Tikhonov y analice, a partir de los resultados anteriores, si resulta conveniente para este problema. Implemente la regularización de orden 0, con $L = I$, que consiste en minimizar

$$\|Ax - b\|_2^2 + \alpha^2 \|x\|_2^2.$$

Analice cómo varía $x_\alpha$ en función del parámetro de regularización $\alpha$. Determine el valor de $\alpha$ que crea adecuado y compare las estimaciones con los resultados obtenidos previamente.

Notebook: `ej4.ipynb` · Figuras: `figuras/`
