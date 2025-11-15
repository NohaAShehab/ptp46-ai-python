"""

global variable can be accessed anywhere in the script
if you want to modify it from inside function/ class

use keyword --> global

"""
track = "AI" # globally in module

print("-- temp string ")

print(track) # read

track = "AI Track"

""" access global variable from function """


def printTrack():
    print(f"-- track  ={track}") # can access global variables

# printTrack()
# printTrack()


""" I want to update track from inside function """

"""
def updateTrack():
    track = input("Please enter track name: ") # define new local variable 
    print(track, "After update")

updateTrack()
print(track)

"""

# use keyword global
def updateTrack():
    global track # please don't create new variable , use the global one
    track = input("Please enter track name: ")
    print(track, "After update")

# updateTrack()
# print(track)
###############################################
"""
    you can define function inside another 
"""
"""
def outerfunction():
    print("******* welcome to outer function ***********")
    name = "Ali"
    print(f"name = {name}")
    def printName():
        # " I can access local variable from inside the inner function"
        print(f"Print the value of name = {name.upper()}")

    printName() # calling the inner function

    def modifyName():
        name = input("please enter name: ") # create new local variable for the inner ??
        print(f"new name  = {name}")

    modifyName()
    print(f"****** name = {name} ******")

outerfunction()
# print(name)
"""

"I need to use the local one of the parent "



def outerfunction():
    print("******* welcome to outer function ***********")
    name = "Ali"
    print(f"name = {name}")
    def printName():
        """ I can access local variable from inside the inner function"""
        print(f"Print the value of name = {name.upper()}")

    printName() # calling the inner function

    def modifyName():
        nonlocal name  # please don't create new one, => use the exisiting
        name = input("please enter name: ")
        print(f"new name  = {name}")

    modifyName()
    print(f"****** name = {name} ******")

outerfunction()
print("---Test----")



def A():
    def B():
        track = "ai"
        def C():
            def D():
                def E():
                    print(track, "from inside E")
                    def F():
                        nonlocal  track
                        track = "Artificial Int... "
                    F()
                E()
            D()
        C()
        print(f"------ track = {track}")
    B()

print("--- Callin gA ")
A()








