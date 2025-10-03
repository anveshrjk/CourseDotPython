from enum import Enum
import sys

age = 20 
print(f"inte is {age} year old")

#concat string
phrase = "inte" + "nooby"

age = str(38)

print("""
    this is line one
      line two 
      .
      .
      .
      line n
        """)

print("inte".upper()) #same for lower
print("inte returns".title()) #capitals first letters
print("inTe".islower())
print("INTE".isupper())

name =  "inteee"
print(name.__len__())
print(len(name))
#both works same

print("in\\te")
print(name[-1])
print(name[0:4])

#complex no.
num1 = 2 + 5j
num2 = complex(2, 5)
print(num1.real, num2.imag)

# ternary operator 
def is_adult(age):
    return True if age > 18 else False

# enums
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)
print(State(0))
print(len(list(State)))

# string slicing
name = "inteee"
print(name[0:4])
print(name[-6:-2])

# string functions
'''
name.endsWith("te") --> boolean type return
name.capitalize() --> 1st char
name.replace(old, new)
name.find(word) --> first appearance index
name.count("e") 
'''