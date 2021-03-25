import unittest
from Operator_searching import search_alg,get_input,read_operator_rate_file

class test_code(unittest.TestCase):

    def setUp(self):
        self.input_string_with_numbers = '+3255416818'



    def test_with_string(self):
        result = get_input(self.input_string_with_numbers)
        self.assertTrue(result, '+3255416818')


