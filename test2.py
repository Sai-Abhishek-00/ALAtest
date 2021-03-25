import unittest
import csv
import random
from Operator_searching import search_alg, get_input, read_operator_rate_file


class test_code(unittest.TestCase):

    def setUp(self):
        self.input_string_with_numbers = random.randint(99, 999999999999999)
        self.test_list = [['25310', '4', 'd'], ['2860', '0.04', 'd'],
                          ['348', '0.4', 'd'], ['2860', '4', 't'],
                          ['2860', '1.23', 'v'], ['405.0', '3', 'a'],
                          ['2860', '0.15', 'a'], ['4050', '4', 's'],
                          ['2860', '1.0', 's'], ['01', '4', 'a'], ]
        self.rate_list = [['1', '0.9', 'a'], ['268', '5.1', 'a'],
                          ['46', '0.17', 'a'], ['4620', '0', 'a'],
                          ['468', '0.15', 'a'], ['4631', '0.15', 'a'],
                          ['4673', '0.9', 'a'], ['46732', '1.1', 'a'],
                          ['1', '0.92', 'b'], ['44', '0.5', 'b'],
                          ['46', '0.2', 'b'], ['467', '1', 'b'],
                          ['48', '1.2', 'b'], ['46', '0.01', 'c']]
        self.test_file_name = 'test_scenarios.csv'
        self.rate_file_name = 'rate_list.csv'

    def test_read(self):
        # test if the file is loading correctly
        resultread = list(read_operator_rate_file(self.rate_file_name))
        self.assertEqual(resultread, self.rate_list)

    def test_searching_alg(self):
        # for a extention with multiple operators
        phone_number = '2860354886'
        result = search_alg(self.test_list, phone_number)
        self.assertEqual(result, None)

    def test_searching_alg1(self):
        # for a extention with decimal operator
        phone_number = '4050'
        result = search_alg(self.test_list, phone_number)
        self.assertEqual(result, None)
        with self.assertRaises(SystemExit):
            # test handling of operator not found
            search_alg(self.test_list, '4051')
        with self.assertRaises(SystemExit):
            # test handling of operator not found
            search_alg(self.test_list, '4')

    def test_input(self):
        # to check if input if being read correctly
        result = get_input(str(self.input_string_with_numbers))
        self.assertTrue(result, str(self.input_string_with_numbers))
        with self.assertRaises(SystemExit):
            # test to check too short input
            get_input('4')
        with self.assertRaises(SystemExit):
            # test to check too long input
            get_input('46354484864634534354354534354354')
        with self.assertRaises(SystemExit):
            # test to check too short input starting with +
            get_input('+4')
        with self.assertRaises(SystemExit):
            # test to check too long input starting with +
            get_input('+46354484864634534354354534354354')
        with self.assertRaises(SystemExit):
            # test to check too string input
            get_input('a46354354354')
        with self.assertRaises(SystemExit):
            # test to check too string input starting with +
            get_input('+a463544354')


if __name__ == '__main__':
    unittest.main()
