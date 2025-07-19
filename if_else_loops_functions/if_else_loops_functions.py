#!/usr/bin/python3
# Test 0; Test a random number if Positive or Negative
'''
import random
nums = random.randint(-10, 10)


def posneg(num):
    if (num > 0):
        print(f"{num} is positive")
    elif (num < 0):
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")


posneg(nums)


# Test 1: assign a random signed number to the variable number
# each time it is executed

number = random.randint(-10000, 10000)


def mod(j):
    return j % 10 if j >= 0 else -(-j % 10)


def assign(n):
    if n > 5:
        return f"{n} and is greater than 5"
    elif n == 0:
        return f"{n} and is 0"
    else:
        return f"{n} and is less than 6 and not 0"


print(f"Last digit of {number} is {assign(mod(number))}")


# Test 2: prints all the a-z in ascii

for i in range(97, 123):
    print(chr(i), end='')

# Test 3: Create a generator to print Test 2 without e and q
print(''.join(c for c in map(chr, range(97, 123)) if c not in ('e', 'q')), end='')

# Test 4: Prints all numbers from 0 to 98 in decimal and in hexadecimal
for i in range(0,99):
    print(f"{i} = ox{i:x}")

# Test 5: Prints number 00-99
for i in range(0, 100):
    if i < 99:
        print(f"{i:02}", end=", ")
    else:
        print(f"{i}")

# Test 6: Prints all possible different combinations of two digits.
for i in range(0, 99):
#    for j in range(len(f"{i}")):
    if i == 23 or i == 11 :
        print(f"{i}", end=", ")
    else:
        continue


# Test 7: a function that checks for lowercase character

def islower(c):
    if c not in map(chr, range(91, 123)):
        return False
    else:
        return True

# Test 8: a function that prints a string in uppercase followed by a new line
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))





#Test 9: A function to print range of prime numbers
def primeRange(num):
    for i in range(num):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

num = int(input("Enter max: "))
primeRange(num)

#Test 10: a function that prints the last digit of a number.
def print_last_digit(number):
    num = f"{number}"
    print(num[len(num)-1])
print_last_digit(23457)
'''

def revprint():
    for i in range(90, 64, -2):
        print("{}".format(chr(i)), end="")
revprint()