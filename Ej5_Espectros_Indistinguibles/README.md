# Ejercicio 5 — Poblaciones distintas con espectros casi indistinguibles

A partir de una composición inicial $x_0 \in \mathbb{R}^{15}$, con $x_0 \ge 0$ y $\mathbf 1^\top x_0 = 1$, construya dos distribuciones de edades distintas $x^{(1)}$ y $x^{(2)}$ ($x^{(i)} \ge 0$, $\mathbf 1^\top x^{(i)} = 1$). Tip: vector de redistribución $d$ con $\mathbf 1^\top d = 0$ y composiciones $x_0 + \tau d$, con $\tau \in \mathbb{R}$.

Utilice una factorización QR para obtener una base ortonormal de las redistribuciones permitidas y la SVD para identificar las que menos modifican el espectro. Las distribuciones deben ser claramente distintas, pero $\|b^{(1)} - b^{(2)}\|_2 < \eta$, con $b^{(1)} = Ax^{(1)}$ y $b^{(2)} = Ax^{(2)}$ los espectros asociados, donde $\eta$ es el nivel de ruido de $b$. Grafique las dos distribuciones y sus espectros. ¿Qué concluye sobre la posibilidad de recuperar una única distribución de edades?

Notebook: `ej5.ipynb` · Figuras: `figuras/`
