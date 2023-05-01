import unittest
from textwrap import dedent

from markupquill import convert


class TestParse(unittest.TestCase):
    def test_matrix(self):
        input_matrix = [['a', 'b'], ['c', 'd']]
        expected = (
            '\\begin{bmatrix}\n'
            'a & b \\\\\n'
            'c & d \\\\\n'
            '\\end{bmatrix}\n'
        )
        actual = convert.matrix(input_matrix)
        self.assertEqual(expected, actual)

    def test_table(self):
        input_matrix = [
            ['a', 'b and so and so', 'c'],
            [
                'd',
                'e',
                'f',
            ],
        ]
        expected = dedent(
            '''
            \\begin{table}[]
            \\begin{tabular}{|l|l|l|}
            \hline
            a & b and so and so & c \\\\
            \hline
            d & e & f \\\\
            \hline
            \end{tabular}
            \end{table}'''
        )
        actual = convert.table(input_matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
