def generate_latex_matrix(matrix: list[list[str]]) -> str:
    """Generate LaTeX code for a matrix"""

    def elements(matrix):
        rows = len(matrix)
        match rows:
            case 0:
                return ''
            case 1:
                return ' & '.join(matrix[0])
            case _:
                return ' & '.join(matrix[0]) + ' \\\\ ' + elements(matrix[1:])

    return '\\begin{bmatrix}' + elements(matrix) + '\\end{bmatrix}'


def parse_matrix_input(input_string):
    """Parse a string of matrix coefficients into a list of lists"""
    rows = input_string.strip().split("\n")
    matrix = [row.split() for row in rows]
    return matrix
