"""
Playground Module
=================
This file serves as a playground for testing and understanding Python functions.
It demonstrates:
- Basic function definitions and calls
- Function execution and memory allocation
- Return values and variable assignment

"""

def sayhello():
    print("hello world ")

# what will happen you call the function ?

"""
when call ==> function---> reserve temp place 
in memory for the function --> to keep varaibles that function need?
until the function finishes its work 
"""

def sumnum(num1, num2):
    res = num1 + num2
    return res

total=sumnum(324,34)
print(total)