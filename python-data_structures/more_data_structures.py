#!/usr/bin/python3
# Test 0: 
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        m=[]
        for j in i:
            j*=j
            m.append(j)
        new_matrix.append(m)
    return new_matrix

square_matrix_simple = __import__('more_data_structures').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Test 1:
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            i = replace
        new_list.append(i)

    return new_list

# Test 2:
def uniq_add(my_list=[]):
    # new_list = set()
    # one = []
    # for i in my_list:
    #     if i not in new_list:
    #         new_list.add(i)
    #         one.append(i)
    return sum(set(my_list))

# Test 3:
def common_elements(set_1, set_2):
    common_elem = {x for x in set_1 if x in set_2}
    return common_elem

# test 4:
def only_diff_elements(set_1, set_2):
    newSet = set_1 ^ set_2
    return newSet

# Test 5:
def number_keys(a_dictionary):
    num = 0
    for key in a_dictionary.keys():
        num += 1
    return num

# Test 6
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")

# Test 7:
def update_dictionary(a_dictionary, key, value):
    if isinstance(key, str):
        a_dictionary[key] = value
    return a_dictionary

# Test 8:
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary and isinstance(key, str):
        del a_dictionary[key]
    return a_dictionary

# Test 9:
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        value *=2
        new_dict[key] = value
    return new_dict

# Test 10:
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)

def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda i: number * i, my_list ))
    return new_list

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    dict = {
        'I' : 1,
        'IV' : 4,
        'V' : 5,
        'IX': 9,
        'X' : 10,
        'XL' : 40,
        'L' : 50,
        'XC': 90,
        'C' : 100,
        'CD': 400,
        'D' : 500,
        'CM': 900,
        'M' : 1000
    }
    if roman_string in dict:
        return dict[roman_string]
    sumn = [dict[x] for x in roman_string if dict[roman_string[0]] >= dict[roman_string[1]]]
    return sum(sumn)

roman_number = "XXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))