import argparse
from markupquill import parse_matrix_input, generate_latex_matrix
from markupquill import parse, convert


def run():
    parser = argparse.ArgumentParser(description='Generate LaTeX for a matrix or table')
    parser.add_argument(
        '--matrix',
        '-m',
        help='Separate matrix elements with spaces, rows with new lines',
    )
    parser.add_argument(
        '--table', '-t', help='Separate columns with "|", rows with new lines'
    )
    args = parser.parse_args()

    if args.matrix is not None:
        matrix = parse.matrix(args.matrix)
        latex_matrix = convert.matrix(matrix)
        print(latex_matrix)
