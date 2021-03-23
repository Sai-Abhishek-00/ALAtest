"""assign call rates to extentions

use dictionary ? or list of lists ? [[extention, rate],[extention, rate]] ?

get a rate list with cheapest rates for each operator

OR

use the dictionary or list list for comparision ?
    a rate lsit would be efficient to check if the operator allows that extention to be called from a single list

parse the phone numbers
switch case starting with max extention numebr until it matches single extentions then state call cannot be completed?
or some other way??

## one long dictionary, with length of original values stored and key position in dictionary act as operator separators
## add an operator identifier to value and use that to identify the name of the operator?
## NO DICTIONARY
##numpy array with csv import.

"""

"""import csv

filename = "OperatorA.csv"
OperatorA = {}
with open(filename, 'r') as operator_data:

    reader = csv.reader(operator_data)
    create_dict_from_csv = {rows[0]:rows[1] for rows in reader}

print(create_dict_from_csv)"""

OperatorA = {1: 0.9, 268: 5.1, 46: 0.17, 4620: 0.0, 468: 0.15, 4631: 0.15, 4673: 0.9, 46732: 1.1}
OperatorB = {1: 0.92, 44: 0.5, 46: 0.2, 467: 1.0, 48: 1.2}
merged_extention_list = []
extention_list = [OperatorA, OperatorB]

for extention in extention_list:
    # [expression for element in iterable if condition]
    merged_extention_list.extend([key for key in extention.keys()])

merged_extention_list = list(set(merged_extention_list))
merged_extention_list_str = [str(x) for x in merged_extention_list]

print("merged list", merged_extention_list)
print("merged_extention_list_str", merged_extention_list_str)

"""USE max() TO FIND THE LONGEST STRING IN A LIST
Call max(a_list, key=len) to return the longest string 
in a_list by comparing the lengths of all strings in a_list."""


"""key: The max function takes an optional argument, key, 
which is the function used to measure the size of the elements of your list. 
Thus, in your case, you're sorting a collection of lists by their length."""
max_extention_length = (len(max(merged_extention_list_str, key=len)))
print("max length", max_extention_length)


def extract_operator_extention(input_number):
    if input_number[0] == '+':
        print("if 1")
        for x in range(max_extention_length + 1, 0, -1):
            if str(input_number[1:x]) in merged_extention_list_str:
                extention_to_dial = input_number[1:x]
                break
    else:
        for x in range(max_extention_length + 1, 0, -1):
            if str(input_number[0:x]) in merged_extention_list_str:
                extention_to_dial = input_number[0:x]
                break
    return (extention_to_dial)


input_number = "+46073059815"
extract_operator_extention(input_number)

# print(input_number[0:max_extention_length+1])
# print(type(merged_extention_list[0]))

