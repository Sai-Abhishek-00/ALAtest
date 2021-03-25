import unittest
import csv
import random
from Operator_searching import search_alg,get_input,read_operator_rate_file

class test_code(unittest.TestCase):

    def setUp(self):
        self.input_string_with_numbers = random.randint(99,999999999999999)
        self.test_list = [['25310', '4', 'd'], ['2860', '0.04', 'd'],
                          ['348', '0.4', 'd'], ['2860', '4', 't'],
                          ['2860', '1.23', 'v'], ['405.0', '4', 'a'],
                          ['2860', '0.15', 'a'], ['4050', '4', 's'],
                          ['2860', '10', 's'], ['01', '4', 'a'],]


    def test_input(self):
        result = get_input(str(self.input_string_with_numbers))
        self.assertTrue(result, str(self.input_string_with_numbers))

    def test_searching_alg(self):
        phone_number = '2860354886'
        result = search_alg(self.test_list, phone_number)
        self.assertEqual(result, None)

    def test_searching_alg(self):
        phone_number = '4050354886'
        result = search_alg(self.test_list, phone_number)
        self.assertEqual(result, None)

    def test_searching_alg(self):
        phone_number = '4051354886'
        result = search_alg(self.test_list, phone_number)
        self.assertEqual(result, None)