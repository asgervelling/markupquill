from textwrap import dedent
import re


def matrix(rows: list[list[str]]) -> str:
    """Generate LaTeX code for a matrix"""
    return f'\\begin{{bmatrix}}\n{_concat_rows(rows)}\n\\end{{bmatrix}}\n'


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
    return f'{start}{_table_header(rows[0])}{_concat_rows(rows[1:])}{end}'


def system_of_equations(aug_matrix: list[list[str]]) -> str:
    """
    Generate LaTeX code for a system of equations,
    based on an augmented matrix.
    """
    print(aug_matrix)
    m = len(aug_matrix)
    n = len(aug_matrix[0])
    num_coefficients = n - 1
    start = '\left\{\n' f'\\begin{{alignedat}}{{{num_coefficients}}}'
    end = '\end{alignedat}\n' '\\right.'

    def line(row: list[str]):
        coefficients = row[:-1]
        constant = row[-1]
        for i, c in enumerate(coefficients):
            if i == 0:
                line_str = f'{coeff(c, i + 1)}'
            else:
                coeff_str = coeff(abs(c), i + 1) \
                            if c < 0 \
                            else coeff(c, i + 1)
                line_str += f'{operator(c)} & {coeff_str}'
        line_str += f' = {constant}'
        return line_str

    def coeff(coefficient: int, index: str):
        if coefficient == 0:
            return '&'
        if coefficient == 1:
            return f'x_{{{index}}} &'
        return f'{coefficient}x_{{{index}}} &'

    def operator(coefficient: int) -> str:
        if coefficient == 0:
            return ''
        return f' -{{}}' if coefficient < 0 else f' +{{}}'

    return (
        f'{start}\n' +
        '\\\\\n'.join([line(row) for row in aug_matrix]) +
        f'\n{end}'
    )

def _table_header(row: list[str]):
    return f"{' & '.join(row)} \\\\\n\\hline\n"


def _concat_rows(rows: list[list[str]]) -> str:
    """Joins a list with the string ' & '"""
    match len(rows):
        case 0:
            return ''
        case 1:
            return f'{" & ".join(rows[0])} \\\\'
        case _:
            return f'{" & ".join(rows[0])} \\\\\n{_concat_rows(rows[1:])}'
