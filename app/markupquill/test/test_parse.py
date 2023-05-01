import unittest
from textwrap import dedent

from markupquill import parse


class TestParse(unittest.TestCase):
    def test_matrix(self):
        input_string = """
            a  b
            c d"""
        expected = [['a', 'b'], ['c', 'd']]
        self.assertEqual(expected, parse.matrix(input_string))
        self.assertEqual(expected, parse.matrix(dedent(input_string)))

    def test_table(self):
        input_string = '''
            a, b and so and so , c 
             d , e , f'''
        expected = [
            ['a', 'b and so and so', 'c'],
            [
                'd',
                'e',
                'f',
            ],
        ]
        self.assertEqual(expected, parse.table(input_string))
        self.assertEqual(expected, parse.table(dedent(input_string)))


if __name__ == '__main__':
    unittest.main()
