"""
Name: Saikiran Rudra
Email: saikiranrudra2@gmail.com
Topic: python assignment 2
"""
import math

# 1. Create the below pattern using nested for loop in Python
def horizontal_pyramid(height: int):
    half = math.ceil(height/2)
    for i in range(1, height + 1):

        if i <= half:
            print("*"*i)
        else:
            print("*"*(height - i + 1))



if __name__ == "__main__":

    #Write a program which accepts a sequence of comma-separated numbers from console  and generate a list
    #question 1
    numbers_string = input("Enter comma seperated numbers: ")
    list_data = list(numbers_string.split(","))
    print(list_data)
    print(f"Data Type of above {type(list_data)}")

    #question 2
    horizontal_pyramid(9)

    #question 3
    #2.  Write a Python program to reverse a word after accepting the input from the user.
    input_string = input("Enter a string: ")
    print(input_string[::-1])