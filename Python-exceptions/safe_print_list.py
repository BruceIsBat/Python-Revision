#!/usr/bin/python3
# Test 0:
def safe_print_list(my_list=None, x=0):
    if my_list is None:
        my_list = []
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            count += 1
        except IndexError:
            break
    print()
    return count

# Test 1:
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Test 2:
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count

# Test 3:
def safe_print_division(a, b):
    div = None
    try:
        div = a/b
    except (ZeroDivisionError, ValueError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
        
# Test 4:
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for a in range(list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print(f"division by 0")
            div = 0
        except IndexError:
            print(f"out of range")
            div = 0
        except TypeError:
            print(f"wrong type")
            div = 0
        finally:
            result.append(div)

    return result

# Test 5: 
def raise_exception():
    raise TypeError

# Test 6:
def raise_exception_msg(message=""):
    raise NameError(message)


# Test 7:
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as f:
        print("Exception: {}".format(f), file=sys.stderr)

