#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Recursive function to calculate the factorial of a given number.

    Parameters:
    - n (int): The number for which factorial is to be calculated.

    Returns:
    - int: The factorial of the input number.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        # Recursive case: Multiply n with factorial of (n-1)
        return n * factorial(n-1)

# Get the input from command line argument
f = factorial(int(sys.argv[1]))
print(f)

