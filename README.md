# latexmatrix
Create a LaTeX matrix from console input

### Usage:
Running
```bash
latexmatrix "
1 2 3
4 5 6"
```
gives you
```bash
\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix}
```

which is LaTex for

$$\begin{bmatrix}1 & 2 & 3 \\\\ 4 & 5 & 6\end{bmatrix}$$

### Installation:
```bash
git clone https://github.com/asgervelling/latex-matrix
cd latex-matrix
pip install .
```

In your LaTeX document, be sure to `\usepackage{amsmath}`.
