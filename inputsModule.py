print("************ welcome to inputs module ***********")
trackname= "AI"
def askForString(message="Please enter string: "):
    while True:
        inStr = input(message)
        if inStr.isalpha():
            return inStr
        print("---- Please enter valid string ")


def askForInt(message="Please enter number: "):
    numm= input(message)
    if numm.isdigit():
        return int(numm)
    print("---- not valid number")
    return  askForInt(message)




"""
every .py file has its main when call it --> it calls __main__
"""
print(__name__, "hereeeeeeeeeeeeeeeeeeeeeeeeee")
if __name__== '__main__':
    # this block will run only if calling the script starts from inputs module
    print(askForString("please enter name: "))
    print(askForInt("please enter age : "))