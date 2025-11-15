"""
Modules and Packages Demonstration
===================================
This file demonstrates how to import and use Python modules and packages.
It covers:
- Importing entire modules
- Importing specific functions from modules
- Importing from packages
- Using aliases for imports
- Package initialization behavior

    any .py file--> is called python module
    ==> you can import module // or part of it ??
"""

# import inputsModule
""" when you import any module --> import blocks and run the executable code """
# call any block
# firstname = inputsModule.askForString("please enter name ")
# print(firstname)


""" I need to import of the module"""
from inputsModule import askForString
# print(askForString("Please enter lastname"))


"""I need to import module from package  """
# import  ai.mathOperations
# print(ai.mathOperations.sumnum(233,2323))

# import  ai.mathOperations as mathmod
# print(mathmod.sumnum(324,32))

""" import part of the module ?"""
from ai.mathOperations import sumnum


# from iti.stringOps import  formatString
# print(formatString("    noha    "))
import ai
""" """
import iti
iti.sayHello()
""" from package import block """
# from iti import sayHello
# from iti import formatString
#
# print(formatString("sdfsdfsf"))