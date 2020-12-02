"""
Name: Saikiran Rudra
Email: saikiranrudra2@gmail.com
Topic: python assignment 3
"""


# 1. Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
def myreduce(fun, lis: list):
    return [fun(i) for i in lis]


# 2. Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
def myfilter(fun, lis: list):
    return [i for i in lis if fun(i)]


if __name__ == "__main__":
    # Question 1 ans
    result = myreduce(lambda x: x ** 2, [1, 2, 3, 4, 5, 6, 7, 8])
    print(result)

    # Question 2 ans
    result = myfilter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(result)

    # Question 3.1 ans
    print([i for i in "ACADGILD"])

    # Question 3.2 ans
    print([i * j for i in ['x', 'y', 'z'] for j in [1, 2, 3]])

    # Question 3.3 ans
    print([i * j for i in [1, 2, 3, 4] for j in ['x', 'y', 'z']])

    # question 3.4 ans
    l1 = [2, 3, 4, 5, 6]
    l3 = [2, 3, 4, 5, 6, 7, 8]
    lis = [[l1[j:j + 3][i]] for j in range(3) for i in range(3)] + [l3[j:j + 4] for j in range(4)]
    print(lis)

    # question 3.5
    print([(j, i) for i in range(1, 4) for j in range(1, 4)])
