# Learning about Functions from Udemy Python course

"""
country = input("Where do you live?")
print("You live in " + country)
"""

# Guessing a number by user input
"""
import random
from tkinter import E
print("I'm thinking of a number between 1 and 10")
thought_number = random.randint(1,10)
number = input("What number am I thinking of?")
number = int(number)
if number == thought_number:
    print("Exactly!")
else:
    print("Please try again, I was thinking of " + str(thought_number))
"""
# Defining a new function
def volume(height, depth, width):
    height_given = int(height)
    depth_given = int(depth)
    width_given = int(width)
    result = height_given * depth_given * width_given
    return result

print("For volume calculation please enter values:")
height_input = input("Height: ")
depth_input = input("Depth: ")
width_input = input("Width: ")
print("Start calculation")
volume_result = volume(height_input, depth_input, width_input)
print("Result: " + str(volume_result))

