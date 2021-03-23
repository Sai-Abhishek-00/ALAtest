import pandas as pd


def read_operator_rate_file(filename):
    rate_list = pd.read_csv(filename, sep=',', header=None).to_numpy()
    return rate_list

filename='rate_list.csv'
rate_list = read_operator_rate_file(filename)

extention_codes_list = [str(extention[0]) for extention in read_operator_rate_file(filename)]

print(extention_codes_list)
max_extention_length = len(max(extention_codes_list, key=len))

def extract_operator_extention(input_number):
    if input_number[0] == '+':
        for x in range(max_extention_length + 1, 0, -1):
            if str(input_number[1:x]) in extention_codes_list:
                extention_to_dial = input_number[1:x]
                break
    else:
        for x in range(max_extention_length + 1, 0, -1):
            if str(input_number[0:x]) in extention_codes_list:
                extention_to_dial = input_number[0:x]
                break
    return (extention_to_dial)

input_number = "+46073059815"
extention_of_input = extract_operator_extention(input_number)

allowed_operators = []
cheapest_call_rate = []

for i in rate_list:
    if str(i[0]) == extention_of_input:
        allowed_operators.append(i)


print(allowed_operators[:1])

def extract