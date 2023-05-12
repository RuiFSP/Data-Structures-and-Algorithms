# my function to check numbers
def check_nums(num1: int, num2: int) -> None:
    """
    Compares two integer values and prints information about their memory addresses.

    Args:
        n1 (int): The first integer value to compare.
        n2 (int): The second integer value to compare.
    """
    print("Before num2 value is updated:")
    print("num1 = ", num1)
    print("num2 = ", num2)

    # check memory address
    print("\nMemory Address of num1 = ", id(num1))
    print("Memory Address of num2 = ", id(num2))
    print("\n")

    if num1 is num2:
        print("num1 and num2 are pointing to the same memory location")
    else:
        print("num1 and num2 are not pointing to the same memory location")


def check_dicts(dict1: dict, dict2: dict) -> None:
    """
    Compares two dictionary values and prints information about their memory addresses.

    Args:
        dict1 (dict): The first dictionary value to compare.
        dict2 (dict): The second dictionary value to compare.
    """
    print("Before dict2 value is updated:")
    print("dict1 = ", dict1)
    print("dict2 = ", dict2)

    # check memory address
    print("\nMemory Address of dict1 = ", id(dict1))
    print("Memory Address of dict2 = ", id(dict2))
    print("\n")

    if dict1 is dict2:
        print("dict1 and dict2 are pointing to the same memory location")
    else:
        print("dict1 and dict2 are not pointing to the same memory location")


print("\nCreating variables - Working with Integers\n")
# we are creating the number 11 in memory, and we point num1 to it.
num1 = 1

# Question 1?  is num2 pointing to same memory location as num1 ?
num2 = num1

check_nums(num1, num2)

# Question 2? what happens if we update num2?
num2 = 2

check_nums(num1, num2)

# Question 3? what happens if we update num1?
num1 = 3

check_nums(num1, num2)

# why does this happen ?
# This happens because Integers are immutable, they cannot be changed once created.
# To change the value of an integer, you need to create a new integer, therefor a  new memory location.
# ------------------------------------------------------------------------------------------------
print("\n------------------------ New Exercise ----------------------------\n")
print("\nCreating variables - Working with dictionaries\n")

# dict1 will point to a directional in memory
dict1 = {"value": 1}
dict2 = dict1

# Question 1? is  dict2 pointing to same memory location as dict1 ?
# yes it is, but let's check it:
check_dicts(dict1, dict2)

# Question 2? what happens if we update de value of dict2?
dict2["value"] = 2

check_dicts(dict1, dict2)

# why does this happen ?
# This happens because dictionaries are mutable, they can be changed once created.
# if you change the value of a dictionary, it will change the value of the dictionary in the memory.
# it will keep the same memory location.
# ------------------------------------------------------------------------------------------------