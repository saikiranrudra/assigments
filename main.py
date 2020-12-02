import math # for pi value
"""
Name: Saikiran Rudra
Email: saikiranrudra2@gmail.com
Topic: Python Assignment 1
"""

"""
1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence 
on a single line.
"""


def divisible_by_7_not_multiple_of_5():
    # in range 3201 is taken instead of 3200 because upper bound is not included
    print([i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0])

"""
2. Write a Python program to accept the user's first and last name and then getting them printed in the the 
reverse order with a space between first name and last name. 
"""

def accept_first_last_name_print_in_reverse():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(first_name[::-1] + " " + last_name[::-1]) ## Printing First and Last name in reverse order


"""
3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula:  V=4/3 * π * r^3
"""


def volume_of_sphere():
    PI = math.pi
    r = 12 / 2
    volume = ( (4 / 3) * PI * (r**2) )
    print(f"Volume of sphere with diameter 12 is {volume}")


if __name__ == "__main__":
    print("Ans for question 1:")
    divisible_by_7_not_multiple_of_5()

    print("Ans for question 2:")
    accept_first_last_name_print_in_reverse()

    print("Ans for question 3:")
    volume_of_sphere()