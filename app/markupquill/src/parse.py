import re


def matrix(input_: str) -> list[list[str]]:
    """Parse a string of matrix coefficients into a list of lists."""
    rows = input_.strip().split("\n")
    return [row.split() for row in rows]


def parse_row(row: str) -> list[str]:
    """
    Turn a string into a list of strings, separated by commas.
    The row can include commas, but those should be escaped
    with a backslash: \,.
    """
    semi_escaped = row.replace('\\,', 'ꙮ')
    cells = semi_escaped.split(',')
    stripped_cells = [cell.strip() for cell in cells]
    # Return the cells with commas escaped
    return [cell.replace('ꙮ', ',') for cell in stripped_cells]


def table(input_: str) -> list[list[str]]:
    """
    Parse a string representing a table
    and turn it into a list of lists.
    """
    rows = input_.strip().split('\n')
    return [parse_row(row) for row in rows]


def system_of_equations(input_: str) -> list[list[str]]:
    """
    Parse a string representing a system of equations.
    Turn it into a list of lists - a matrix.
    """
    pass