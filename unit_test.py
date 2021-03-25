"""assert equals
assert type(var) is int/str
"""

import unittest
from main import read_operator_rate_file, get_input, get_max_extention_length, extract_operator_extention, cheapest_call_rate, print_output

class unit_test(unittest.TestCase):
    def setUp(self):
        self.file_does_exist = 'no_file.csv'
        self.input_string_with_numbers = '+325a16818'
        self.input_string_with_symbols = '+sfe,)(/"&#'
        self.input_wrong_length_long = 561651651616151651531287986
        self.input_wrong_length_short = 12

    def test_load_file(self):
        with self.assertRaises(Exception):
            read_operator_rate_file(self.file_does_exist)


    def test_input_parameters(self):



    def test_read_input

    if __name__ == '__main__':
        unittest.main()
