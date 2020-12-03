"""
Name: Saikiran Rudra
Email: saikiranrudra2@gmail.com
Topic: Exception handling Assignment
"""

if __name__ == "__main__":
    # 1. Write a function to compute 5/0 and use try/except to catch the exceptions.
    try:
        print(5/0)
    except ZeroDivisionError as e:
        print(e)

    # 2. Implement a Python program to generate all sentences where subject is in
    # ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
    # ["Baseball","cricket"].
    # Hint: Subject,Verb and Object should be declared in the program as shown below.

    subjects = ["Americans", "Indians"]
    verbs = ["play", "watch"]
    objects = ["Baseball", "Cricket"]
    sentences =[ f"{i} {j} {k}" for i in subjects for j in verbs for k in objects ]

    for sentence in sentences:
        print(sentence)