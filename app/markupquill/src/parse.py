def matrix(input_: str) -> list[list[str]]:
    """Parse a string of matrix coefficients into a list of lists."""
    rows = input_.strip().split("\n")
    return [row.split() for row in rows]


# def table(input_: str) -> list[list[str]]:
#     """
#     Parse a string representing a table
#     and turn it into a list of lists.
#     """
#     rows = input_.strip().split('\n')
#     str_operations = [
#         str.strip,
#         lambda s: s.replace('\\,', ','),
#         str.split,
#     ]
#     parse_row = lambda row: map(str.strip, row.split(','))
#     return [list(parse_row(row)) for row in rows]

def parse_row(row: str) -> list[str]:
    cells = row.split(',')
    stripped_cells = [cell.strip() for cell in cells]
    return [cell.replace('\\,', ',') for cell in stripped_cells]


def table(input_: str) -> list[list[str]]:
    """
    Parse a string representing a table
    and turn it into a list of lists.
    """
    rows = input_.strip().split('\n')
    return [parse_row(row) for row in rows]