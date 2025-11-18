#!/usr/bin/python3
# Test 0: A program that imports the function def add(a, b): from the file add_0.py
'''from add_0 import add
a = 1
b = 2
result = add(a, b)
print(f"{a} + {b} = {result}")


# Test 1: A program that imports functions from the file calculator_1.py, 
#does some Maths, and prints the result.
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")


# Test 2: A program that prints the number of and the list of its arguments.
import sys

 

if len(sys.argv)-1 ==1:
    print(f"{len(sys.argv)-1} argument:")
    
elif len(sys.argv)-1 > 1:
    print(f"{len(sys.argv)-1} arguments:")
else:
    print(f"{len(sys.argv)-1} arguments.")


for i in range(1, len(sys.argv)):
    print(f"{i}: {sys.argv[i]}")

# Test 3: A program to prints the result of the addition of all arguments
n =[]
for i in range(1, len(sys.argv)):
    n.append(int(sys.argv[i]))
print(sum(n))



# Test 4:
import sys
from calculator_1 import add, sub, mul, div

def main():
    arg = sys.argv
    a, b = map(int, (arg[1], arg[3]))

    if len(arg) > 4:
        print(f"./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if arg[2] not in ('+', '-', '*', '/'):
        print(f"unknown operator. Available operators; +, -, *, /")
        sys.exit(1)
    if arg[2]=='+':
        print(f"{a} + {b} = {add(a,b)}")
    elif arg[2]=='-':
        print(f"{a} - {b} = {sub(a,b)}")
    elif arg[2]=='*':
        print(f"{a} * {b} = {mul(a,b)}")
    elif arg[2]=='/':
        print(f"{a} / {b} = {div(a,b)}")
        
    
if __name__ == "__main__":
    main()


# Test 5: 
import importlib.util

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", '/home/keji/Python-Revision/import_modules/hidden_4.pyc')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # List and filter names
    names = [name for name in dir(module) if not name.startswith('__')]
    
    # Sort and print
    for name in sorted(names):
        print(name)

# Test 6: 
from variable_load_5 import a
if __name__ == "__main__":
    print(f"{a}")

# __builtins__.__dict__['printf'] = __builtins__.__dict__['__stdout__.write']
# printf("#pythoniscool")
import os
os.write(1, b"#pythoniscool\n")
'''

import add_0, dis
print(dis.dis(add_0))
