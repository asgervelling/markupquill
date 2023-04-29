import argparse
from latexmatrix import parse_matrix_input, generate_latex_matrix


def run():
    parser = argparse.ArgumentParser(description="Generate LaTeX code for a matrix")
    parser.add_argument(
        "matrix_input",
        help="matrix coefficients (one row per line, separate coefficients with spaces)",
    )
    args = parser.parse_args()
    matrix = parse_matrix_input(args.matrix_input)
    latex_matrix = generate_latex_matrix(matrix)
    print(latex_matrix)
