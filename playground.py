# import sys
# import os
# print(os.system('ls -l '))

# open file --> then close after the operation
with open("users.txt", "w") as fileobj:
    mode = fileobj.mode
    fileobj.write("hello")

print(fileobj, mode)

# print(fileobj.read())


try:
    newfile=  open("newfile.txt", "w")
except Exception as e:
    print(e)
else:
    print(newfile)


