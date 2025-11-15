"""
String Operations Module
=========================
This module contains utility functions for string manipulation.
Currently includes a function to format strings by stripping whitespace
and converting to title case.
"""


def formatString(anystr: str):
    if isinstance(anystr, str):
        return  anystr.strip().title()
    print("--- not vali string ")
    return False
