"""
Math Operations Module
======================
This module contains mathematical operation functions.
Currently includes a function to sum two integers with input validation.
"""

def sumnum(num1:int, num2:int)-> int:
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        return res
    print("---- not valid inputs ")
    return 0