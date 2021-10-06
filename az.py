import os
import math
import json


os.system("whoami")
look = os.getcwd()
print(look)
os.listdir()
look1 = os.mkdir("New Folder1")
print(look1)
os.listdir()
os.rmdir("New Folder1")
os.getlogin()



absolute = -5.999
floor_test = 198.42

result1 = math.fabs(absolute)
result2 = math.floor(floor_test)

print(result1, " is the absolute value of ", absolute)
print(result2, " is the flow of ", floor_test)


filename = 'userName.json'
name = ''
try:
    with open(filename, 'r') as r:
        name = json.load(r)
except IOError:
    print("First-time login")
if name != "":
    print("Welcome back, " + name + "!")
else:
    name = input("Hello! What's your name? ")
    print("Welcome, " + name + "!")

try:
    with open(filename, "w") as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")