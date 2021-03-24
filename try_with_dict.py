import csv
def read_operator_rate_file(filename):
    try:
        with open(filename, newline='') as f:
            return list(csv.reader(f))
    except FileNotFoundError as errorcode:
        print(errorcode)

def get_input():
    while True:
        try:
            phone_number_to_dial = input("Enter phone number>> ")
            assert (phone_number_to_dial.startswith('+') and phone_number_to_dial[1:].isdigit()) or  phone_number_to_dial[:].isdigit(), 'Invalid phone number, Enter again or press ctrl+c to exit'
        except Exception as e:
            print(e)
        else:
            return(phone_number_to_dial)

def get_max_extention_length(rate_list):
    extention_codes_list = [str(extention[0]) for extention in rate_list]
    return extention_codes_list,len(max(extention_codes_list, key=len))

def extract_operator_extention(input_number):
    extention_to_dial = "Operator not found"
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

def cheapest_call_rate(dialing_operator):
    allowed_operators = []
    for i in rate_list:
        if str(i[0]) == dialing_operator:
            allowed_operators.append(i)
    return min(allowed_operators)


if __name__ == '__main__':
    filename = 'rate_list.csv'
    rate_list = read_operator_rate_file(filename)
    extention_codes_list,max_extention_length = get_max_extention_length(rate_list)
    input_number = get_input()
    dialing_operator = extract_operator_extention(input_number)
    if dialing_operator == "Operator not found":
        print(dialing_operator)
        exit()
    price = cheapest_call_rate(dialing_operator)[1]
    operator = cheapest_call_rate(dialing_operator)[2]
    print("cheapest price is", price, "with the operator", operator)