"""

    any content defined in the __init__ file is called automatically
    when you import any module from pacakge or part of module .
"""

print("--- Hello welcome to ITI package ----")

def sayHello():
    print("********* Hello Dearest User **************")

"""
when you define __init__ inside the package => python treats package
 as a module with the name of the package
"""

"""
I can use this file as index. entry point for the packages 

"""
# import the function inside the __init__
# from iti.stringOps import  formatString