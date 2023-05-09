import unittest
from textwrap import dedent

from markupquill import convert


class TestParse(unittest.TestCase):
    def test_matrix(self):
        input_matrix = [['a', 'b'], ['c', 'd']]
        expected = '\\begin{bmatrix}\n' 'a & b \\\\\n' 'c & d \\\\\n' '\\end{bmatrix}\n'
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

    def test_system_of_equations(self):
        aug_matrix = [
            ['-2', '132', '-3', '10'],
            ['1', '0', 'a^2', '6'],
            ['321321', '3', '2', '13'],
        ]
        expected = (
            '\left\{\n'
            + '\\begin{alignedat}{3}\n'
            + '-2x_{1} & +{} & 132x_{2} & -{} & 3x_{3} & = 10\\\\\n'
            + 'x_{1} & & & +{} & a^2x_{3} & = 6\\\\\n'
            + '321321x_{1} & +{} & 3x_{2} & +{} & 2x_{3} & = 13\n'
            + '\end{alignedat}\n'
            + '\\right.'
        )
        actual = convert.system_of_equations(aug_matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
