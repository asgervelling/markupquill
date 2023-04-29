def matrix(m: list[list[str]]) -> str:
    """Generate LaTeX code for a matrix"""

    def elements(m):
        rows = len(m)
        match rows:
            case 0:
                return ''
            case 1:
                return ' & '.join(m[0])
            case _:
                return ' & '.join(m[0]) + ' \\\\ ' + elements(m[1:])

    return '\\begin{bmatrix}' + elements(m) + '\\end{bmatrix}'


def table(t: list[list[str]]) -> str:
    """Generate LaTeX code for a table"""
    pass
