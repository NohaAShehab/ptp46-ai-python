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


# # exit(2)
# print(34/0)

try:
    num1 = int(input("please enter first number "))
    num2 = int(input("please enter second number"))
    res = num1/num2
    print(res)
    # you may receive exceptions from different types
    # so may need to change how will you handle it .
    # you can add more than one except ?
except Exception as e :  # object contain exception details
    print(f"--- error happened {e}")
    print(e.__dict__,e.__repr__())