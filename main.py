"""Not adding constraints to phone number length as it varies from country to country
and also extention phones such as in hotel or offices have only single digit calling features"""
import csv


def read_operator_rate_file(filename):
    """This function reads the file with operators and their prices
    The variable filename contains the name of csv with operator list"""
    try:
        with open(filename, newline='') as f:
            return list(csv.reader(f))
    except FileNotFoundError as errorcode:
        print(errorcode)


def get_input():
    """Function to read user input
    Excepting a phone number
    May start with '+' or only digits
    Added conditions to check for strings or other invalid variables in the input
    """
    while True:
        try:
            phone_number_to_dial = input("Enter phone number>> ")
            assert (phone_number_to_dial.startswith('+') and phone_number_to_dial[
                                                             1:].isdigit()) or phone_number_to_dial[
                                                                               :].isdigit(), 'Invalid phone number'
        except Exception as e:
            print(e)
        else:
            return (phone_number_to_dial)


def get_max_extention_length(rate_list):
    """This function serves two tasks.
    1. Extract extentions of allowed operators from the Rate List.
    2. Get the length of the maximum extention in the Rate List.
    """
    extention_codes_list = [str(extention[0]) for extention in rate_list]
    return extention_codes_list, len(max(extention_codes_list, key=len))


def extract_operator_extention(input_number):
    """This funstion checks if the extention entered by the user is in the Rate List or not.
    If present, then returns the extention otherwise send an message if that the operator is not valid
    """
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
    """Function to get all possible operators who allow calling to a certain extention
    The allowed operators list will contain a list of lists in the format [extention, rate, operator]
    """
    allowed_operators = []
    for i in rate_list:
        if str(i[0]) == dialing_operator:
            allowed_operators.append(i)
    return min(allowed_operators)


if __name__ == '__main__':
    filename = 'rate_list.csv'  # variable with csv filename
    rate_list = read_operator_rate_file(
        filename)  # rate list has the information from csv file, it contains all the [extention, rate, operator]
    extention_codes_list, max_extention_length = get_max_extention_length(
        rate_list)  # extention_code_list has only the allowed extentions by operator. This is to minimize operations on list of lists
    input_number = get_input()  # store the user defined phone number for which the rate needs to be checked
    dialing_operator = extract_operator_extention(
        input_number)  # Store only the operator of the user entered phone number
    if dialing_operator == "Operator not found":
        print(dialing_operator)
        exit()
    price = cheapest_call_rate(dialing_operator)[1]  # Store the cheapest price for a certain extention
    operator = cheapest_call_rate(dialing_operator)[2]  # Store the operator with cheapest price for a certain extention
    print("cheapest price is", price, "with the operator", operator)  # Show the output.
