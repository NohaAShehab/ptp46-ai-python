# def sayHello():
#     print("testttttttt")
#     return  "Ahmed AbdElNaby"
#
# s1 = {
#     "name":"Ahmed",
#     "track": "ai",
#     "fun": sayHello
#
# }
#
# print(s1)
# print(s1["fun"]())

#########################


s1 = {
    "name":"Ahmed",
    "track": "ai",
    "age":23
}

s2 = {
    "stdname": 'ali',
    "track": 'ai',
    "Age": 24
}



def displayStudent(std):
    print(f"name={std['name']}, age={std['age']}")

displayStudent(s1)


"""
You need to create your own datatype 
simply create class ?? 

--> define common properties --> in all objects 
==> apply common functionality ===> to all objects 
"""


# class Student:
#     pass
#
# s = Student() # take an object --> reserve new place in memory
# print(s)  # <__main__.Student object at 0x7752450fbcb0>
#
# # loosely - dynamically typed lang. =
# s.name= "Ahmed"
# s.email = 'ahmed@gmail.com'
# s.salary  = 100000  # add data to object in the runtime
# import  sys
# print(sys.getsizeof(s))
#
# s2= Student()
# s2.name= 'Ali'
# s.email = 'Ali@gmail.com'
# s2.salary = 2000
# print(s2)
# print(sys.getsizeof(s2))
#
#
#
#
# s3= Student()
# s3.name = 'mohamed'
# print(s3)
#
#
# s5 = Student()
# s5.track = "Ai"
# s5.courses = ["python", "test", "abc"]
# print(sys.getsizeof(s5), "s5")
#
# s6= Student()
# print(sys.getsizeof(s6))


"****************************************************"


class Student:
    def __init__(self):
        self.name = 'Ahmed'
        self.email = 'ahmed@gmail.com'
        self.salary = 20000


std1 = Student()
std2 = Student()





