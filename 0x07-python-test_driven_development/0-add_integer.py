#!/usr/bin/python3
"""
Module 0-add_integer
Contains one method that accepts two values of int or float type,
casts them to int before adding, and returns the sum as an integer.
"""

def add_integer(a, b=98):
    """
    Return the sum of two arguments.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number, default is 98.
        
    Returns:
        int: The sum of a and b after casting them to integers.
        
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a == float('inf') or a != a):  # Check for infinity and NaN
        raise ValueError("cannot convert float infinity to integer" if a == float('inf') else "cannot convert float NaN to integer")
    if isinstance(b, float) and (b == float('inf') or b != b):  # Check for infinity and NaN
        raise ValueError("cannot convert float infinity to integer" if b == float('inf') else "cannot convert float NaN to integer")

    return int(a) + int(b)

