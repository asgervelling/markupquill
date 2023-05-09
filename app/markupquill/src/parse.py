import re


def matrix(input_: str) -> list[list[str]]:
    """Parse a string of matrix coefficients into a list of lists."""
    rows = input_.strip().split("\n")
    return [row.split() for row in rows]


def parse_row(row: str, delimiter_char=',') -> list[str]:
    """
    Turn a string into a list of strings,
    separated by the delimiter char (default: ',').
    Delimiter chars may be escaped with a backslash: \,.
    """
    semi_escaped = row.replace(f'\\{delimiter_char}', 'ꙮ')
    cells = semi_escaped.split(delimiter_char)
    stripped_cells = [cell.strip() for cell in cells]
    # Return the cells with commas escaped
    return [cell.replace('ꙮ', delimiter_char) for cell in stripped_cells]


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
