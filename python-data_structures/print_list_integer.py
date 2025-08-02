#!/usr/bin/python3
# Test 0: 
def print_list_integer(my_list=[]):
    for a in my_list:
        print("{}".format(a))

# Test 2: 
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list)-1:
        return None
    else:
        return my_list[idx]

# Test 3:
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list)-1:
        return my_list
    else:
        my_list[idx] = element
        return my_list

# Test 4: 
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print(i)
# Test 5:
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return my_list
    elif idx > len(my_list)-1:
        return my_list
    else:
        new_list[idx] = element
        return new_list

# Test 6: 
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if i not in ('c', 'C'):
            new_string += i
    return new_string

# Test 7: 
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{}".format(j), end='')
        print()

# Test 8:
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)

# Test 9:
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

# Test 10:
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    max_integer = my_list[0]
    for i in my_list:
        if i > max_integer:
            max_integer = i
    return max_integer

# Test 11:
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

#Test 12:
def delete_at(my_list=[], idx=0):
    wid = len(my_list)
    # new_list=[]
    # if idx < 0 or idx >= wid:
    #     return my_list
    # for i in range(wid):
    #     if i == idx:
    #         continue
    #     new_list.append(my_list[i])
    # return new_list
    if 0 <= idx < wid:
        del my_list[idx]
    return my_list

#Test 13:
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
