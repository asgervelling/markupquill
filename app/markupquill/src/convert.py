from textwrap import dedent


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
    num_columns = max(map(len, t))
    example = """
        \begin{table}[]
        \begin{tabular}{lll}
        ID & Name             & Country \\
        1  & Elizabeth Turner & UK      \\
        2  & Bob Adam         & Sweden 
        \end{tabular}
        \end{table}
    """
    def elements(m):
        rows = len(m)
        match rows:
            case 0:
                return ''
            case 1:
                return f'{" & ".join(m[0])} \\\\'
            case _:
                return f'{" & ".join(m[0])} \\\\\n{elements(m[1:])}'
            
    
    borders = f'|{"l|" * num_columns}'
    start = dedent(f'''
        \\begin{{table}}[]
        \\begin{{tabular}}{{{borders}}}
    ''')
    end = dedent('''
        \\end{tabular}
        \\end{table}''')
    return f'{start}{elements(t)}{end}'