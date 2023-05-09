import argparse
from markupquill import parse, convert


def run():
    parser = argparse.ArgumentParser(description='Generate LaTeX for a matrix or table')
    parser.add_argument(
        '--matrix',
        '-m',
        help='Separate matrix elements with spaces, rows with new lines',
    )
    parser.add_argument(
        '--table',
        '-t',
        help='Separate columns with commas, rows with new lines',
    )
    parser.add_argument(
        '--system',
        '-s',
        help='System of equations.\n' +
             'Separate coefficients and constants from variables ' +
             'with spaces, one equation per line.'
    )
    args = parser.parse_args()

    if args.matrix is not None:
        matrix = parse.matrix(args.matrix)
        latex_matrix = convert.matrix(matrix)
        print(latex_matrix)

    if args.table is not None:
        table = parse.table(args.table)
        latex_table = convert.table(table)
        print(latex_table)

    if args.system is not None:
        system = parse.system_of_equations(args.system)
        latex_system = convert.system_of_equations(system)
        print(latex_system)
