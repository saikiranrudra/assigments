"""
Name: Saikiran Rudra
Email: saikiranrudra2@gmail.com
Topic: python assignment 4
"""


# 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
class Shape:
    _s = None
    _a = None
    _b = None
    _c = None

    def get_dimension(self):
        self._s = int(input("Enter the value of s: "))
        self._a = int(input("Enter the value of a: "))
        self._b = int(input("Enter the value of b: "))
        self._c = int(input("Enter the value of c: "))


class Triangle(Shape):

    def calculate_area(self):
        return (self._s * (self._s - self._a) * (self._s - self._b) * (self._s - self._c)) ** 0.5


# 1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words
# that are longer than n
filter_long_words = lambda words, n: [word for word in words if len(word) > n]

# 2.1  Write a Python program using function concept that maps list of words into a list of integers  representing the
# lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are
# the lengths of the words in the list.
map_word_to_int = lambda words: [len(word) for word in words]

# 2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if  it is a vowel, False
# otherwise.
is_vowel = lambda char : char in "aeiou"

if __name__ == "__main__":

    # question 1.1
    triangle = Triangle()
    triangle.get_dimension()
    print(triangle.calculate_area())

    # quesrion 1.2
    words = ["big", "bigger", "biggerr", "biggerrr", "biggerrrr"]
    print(filter_long_words(words, 6))

    # question 2.1
    print(map_word_to_int(["word", "bigWord", "biggerWord", "veryBiggerrrWord"]))

    # question 2.2
    print(is_vowel('o'))

