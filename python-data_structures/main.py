#!/usr/bin/python3
"""print_list_integer = __import__('print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
element_at = __import__('print_list_integer').element_at

my_list = [1, 2, 3, 4, 5]
idx = 2
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

replace_in_list = __import__('print_list_integer').replace_in_list
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

print_reversed_list_integer = __import__('print_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

import timeit

setup = "my_list = list(range(10000))"

print(timeit.timeit('for x in reversed(my_list): pass', setup=setup, number=1000))
print(timeit.timeit('for x in my_list[::-1]: pass', setup=setup, number=1000))
print(timeit.timeit('i=len(my_list)-1\nwhile i>=0:\n x=my_list[i]\n i-=1', setup=setup, number=1000))


new_in_list = __import__('print_list_integer').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

no_c = __import__('print_list_integer').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))


print_matrix_integer = __import__('print_list_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()


add_tuple = __import__('print_list_integer').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))


max_integer = __import__('print_list_integer').max_integer

my_list = [1, 90, 2, 13, 340, 5, -1300, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))


divisible_by_2 = __import__('print_list_integer').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

delete_at = __import__('print_list_integer').delete_at

my_list = [1, 2, 3, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

square_matrix_simple = __import__('more_data_structures').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

search_replace = __import__('more_data_structures').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

uniq_add = __import__('more_data_structures').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
print(type(result))

# print(list(map(lambda x: x*x, [1, 2, 3, 4, 5])))

import random
num = range(1, 100)
func = lambda x : x % 9==0
print(list(filter(func, num)))

common_elements = __import__('more_data_structures').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))


only_diff_elements = __import__('more_data_structures').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

number_keys = __import__('more_data_structures').number_keys
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level", 'age': 23 }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
"""
print_sorted_dictionary = __import__('more_data_structures').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)