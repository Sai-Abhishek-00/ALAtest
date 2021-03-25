import csv


def read_operator_rate_file(filename):
    """This function reads the file with operators and their prices
    The variable filename contains the name of csv with operator list"""
    try:
        with open(filename, newline='') as f:
            return list(csv.reader(f))  # read each row as a list and store it in a list
    except FileNotFoundError as errorcode:
        print(errorcode)
    except IOError:
        print("Could not read file:"), filename


def get_input(phone_number_to_dial):
    """Function to read user input
    Excepting a phone number
    May start with '+' or only digits
    Added conditions to check for strings or other invalid variables in the input
    """
    while True:
        try:

            """check if the input starts with a '+' sign, then all digits except for first should be integer. 
            Since the input with '+' is considered as String parse one character at a time and check if they are ints. 
            """
            assert (phone_number_to_dial.startswith('+') and phone_number_to_dial[
                                                             1:].isdigit()) or phone_number_to_dial[
                                                                               :].isdigit(), 'Invalid phone number'
            assert len(
                phone_number_to_dial) > 2, 'Phone number too short'
            # had this at 9 but changed it to 2 for calling 112
            assert len(phone_number_to_dial) < 16, 'Phone number too long'
        except Exception as e:
            print(e)
            exit()
        else:
            return (phone_number_to_dial)


def search_alg(rate_list, input_number):
    def get_max_extention_length(rate_list):
        """This function serves two tasks.
        1. Extract extentions of allowed operators from the Rate List.
        2. Get the length of the maximum extention in the Rate List.
        """
        extention_codes_list = [str(extention[0]) for extention in rate_list]
        return extention_codes_list, len(max(extention_codes_list, key=len))

    def extract_operator_extention(input_number):
        """This function checks if the extention entered by the user is in the Rate List or not.
        If present, then returns the extention otherwise send an message if that the operator is not valid
        """
        extention_to_dial = "Operator not found"
        if input_number[0] == '+':
            for x in range(max_extention_length + 1, 1, -1):
                """Breaking the phone number into extention and number. 
                Read the input in reverse order starting from the max extention length in the rate list.
                This is to avoid taking operators based on first digit alone."""
                if str(input_number[
                       1:x]) in extention_codes_list:  # check if parsed string is a operator by checking the extention list
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
        allowed_operators = []  # List to store the operators which allow calling to the desired extention
        for i in rate_list:
            if str(i[0]) == dialing_operator:
                allowed_operators.append(i)
        return min(allowed_operators)  # Return only the lsit with min rate

    def print_output():
        """"Function to print output with conditions"""
        try:
            extention_dialing = cheapest_call_rate(dialing_operator)[0]
            price = cheapest_call_rate(dialing_operator)[1]
            # Store the cheapest price for a certain extention
            operator = cheapest_call_rate(dialing_operator)[2]
            # Store the operator with cheapest price for a certain extention
        except Exception as e:
            print(e)
        else:
            print("To call the extention +", extention_dialing, "the cheapest price is", price, "with the operator",
                  operator)
            # Show the output.

    extention_codes_list, max_extention_length = get_max_extention_length(rate_list)
    # extention_code_list has only the allowed extentions by operator. This is to minimize operations on list of lists
    dialing_operator = extract_operator_extention(input_number)
    # Store only the operator of the user entered phone number
    if dialing_operator == "Operator not found":
        print(dialing_operator)
        exit()
    print_output()


if __name__ == '__main__':
    # variable with csv filename
    filename = 'rate_list.csv'
    # store the user defined phone number for which the rate needs to be checked
    phone_number_to_dial = input("Enter phone number>> ")
    input_number = get_input(phone_number_to_dial)
    # rate list has the information from csv file, it contains all the [extention, rate, operator]
    rate_list = read_operator_rate_file(filename)
    search_alg(rate_list, input_number)