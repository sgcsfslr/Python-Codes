# Quadratic.py
# Reference from China University Python Module
# This program is not perfect enough

import math
def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients(a, b, c): "))
    delta = b * b - 4 * a * c
    if delta >= 0:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    if delta < 0:
        print("The equation has no real roots!")


main()
