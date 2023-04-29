def matrix(input_string):
    """Parse a string of matrix coefficients into a list of lists."""
    rows = input_string.strip().split("\n")
    matrix = [row.split() for row in rows]
    return matrix


def table(input_string):
    """
    Parse a string representing a table
    and turn it into a list of lists.
    """
    pass