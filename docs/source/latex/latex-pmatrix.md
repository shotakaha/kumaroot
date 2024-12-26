# 行列したい（`pmatrix`）

```latex
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
```

`pmatrix`環境で行列を出力できます。

## CKM行列したい

小林・益川行列は次のように出力できます。

```latex
\begin{align}
V_{\text{CKM}} =
\begin{pmatrix}
V_{\text{ud}} & V_{\text{us}} & V_{\text{ub}} \\
V_{\text{cd}} & V_{\text{cs}} & V_{\text{cb}} \\
V_{\text{td}} & V_{\text{ts}} & V_{\text{tb}}
\end{pmatrix}
\end{align}
```

:::{math}
V_{\text{CKM}} =
\begin{pmatrix}
V_{\text{ud}} & V_{\text{us}} & V_{\text{ub}} \\
V_{\text{cd}} & V_{\text{cs}} & V_{\text{cb}} \\
V_{\text{td}} & V_{\text{ts}} & V_{\text{tb}}
\end{pmatrix}
:::

Wolfenstein表記は次のように出力できます。

```latex
\begin{align}
V_{\text{CKM}} \approx
\begin{pmatrix}
1 - \frac{\lambda^{2}}{2} & \lambda & A \lambda^{3} (\rho - i \eta) \\
- \lambda & 1 - \frac{\lambda^{2}}{2} & A \lambda^{2} \\
A \lambda^{3} (1 - \rho - i \eta) & -A \lambda^{2} & 1
\end{pmatrix}
\end{align}
```

:::{math}
V_{\text{CKM}} \approx
\begin{pmatrix}
1 - \frac{\lambda^{2}}{2} & \lambda & A \lambda^{3} (\rho - i \eta) \\
- \lambda & 1 - \frac{\lambda^{2}}{2} & A \lambda^{2} \\
A \lambda^{3} (1 - \rho - i \eta) & -A \lambda^{2} & 1
\end{pmatrix}
:::
