from textwrap import dedent


def matrix(rows: list[list[str]]) -> str:
    """Generate LaTeX code for a matrix"""
    return '\\begin{bmatrix}' + concat_rows(rows) + '\\end{bmatrix}'
        

def table(rows: list[list[str]]) -> str:
    """Generate LaTeX code for a table"""
    num_columns = max(map(len, rows))
    borders = f'|{"l|" * num_columns}'
    start = dedent(
        f'''
        \\begin{{table}}[]
        \\begin{{tabular}}{{{borders}}}
        \\hline
    '''
    )
    end = dedent(
        '''
        \\hline
        \\end{tabular}
        \\end{table}'''
    )
    return f'{start}{table_header(rows[0])}{concat_rows(rows[1:])}{end}'


def table_header(row: list[str]):
    return f"{' & '.join(row)} \\\\\n\\hline\n"


def concat_rows(rows: list[list[str]]) -> str:
    """Joins a list with the string ' & '"""
    match len(rows):
        case 0:
            return ''
        case 1:
            return ' & '.join(rows[0])
        case _:
            return f'{" & ".join(rows[0])} \\\\\n{concat_rows(rows[1:])}'
