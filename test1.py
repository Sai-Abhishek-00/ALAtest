import unittest

from main import get_max_extention_length, cheapest_call_rate, read_operator_rate_file, print_output, get_input


class TestNoneIsFalse(unittest.TestCase):
    def setUp(self):
        self.file_does_not_exist = 'no_file.csv'
        self.input_string_with_numbers = '+325a16818'
        self.input_string_with_symbols = '+sfe,)(/"&#'
        self.input_wrong_length_long = 561651651616151651531287986
        self.input_wrong_length_short = 12
        self.rate_list = [['1', '0.9', 'a'], ['268', '5.1', 'a'],
                          ['46', '0.17', 'a'], ['4620', '0', 'a'],
                          ['468', '0.15', 'a'], ['4631', '0.15', 'a'],
                          ['4673', '0.9', 'a'], ['46732', '1.1', 'a'],
                          ['1', '0.92', 'b'], ['44', '0.5', 'b'],
                          ['46', '0.2', 'b'], ['467', '1', 'b'],
                          ['48', '1.2', 'b'], ['46', '0.01', 'c'],
                          ['268', '4.1', 'c']]
        self.extention_price_test1 = ['1']
        self.extention_price_test2 = ['268']
        self.extention_price_test3 = ['46']sdfdd


    def test_reading_max_extention_length(self):
        result = get_max_extention_length(self.rate_list)
        self.assertEqual(result[1], 5)

    def test_case_1(self):
        var0 = '~29Dq\\G'
        var1 = get_max_extention_length(var0)
        assert var1 is not None

    def test_case_2(self):
        var0 = '~29Dq\\G'
        var1 = get_max_extention_length(var0)
        assert var1 is not None
        var2 = get_input()

    def test_case_3(self):
        var0 = '~29Dq\\G'
        var1 = get_max_extention_length(var0)
        assert var1 is not None
        var2 = get_input()
        var3 = print_output()
        var4 = '~29Dq\\G'
        var5 = get_max_extention_length(var4)
        var6 = False
        var7 = get_max_extention_length(var6)


