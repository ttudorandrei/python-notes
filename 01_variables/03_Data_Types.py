# Numeric data types
#
# i = 375  #int
# f = 3.75  # float
# c = 3j + 2  # complex number
#
# print(c, type(c))
# add = 3 + 5
# subtract = 8 - 4
# multiply = 7 * 9
# divide = 9 / 3
# power_of = 3 ** 2  # 3 to the power of 2
# modulo = 10 % 4  # gives the remainder after division
# square_root = (25 ** 1/2)  # returns the square root
# cube_root = (25 ** 1/3)  # returns the cube root
#
# print(13 % 3)  # returns one (3 fits in 13 4 times and returns a remainder of 1)
# print(12 % 3)  # returns 0 (three fits in 12 4 times and nothing is left after)
#
# print(14 // 3, 14 % 3)
#
# print(13 // 4)  # returns the result as an int (as opposed to the simple division that would return 4.333etc)
# third = 1 / 3
# print(third)

# String data types
#
# single = 'String in single quotes'
# double = "string in double quotes"
# # can not mix single and double quotes
# single_in_double = "This is Tudor's string"
# double_in_single = 'This is "a quote"'
# both = "This is Tudor's \"string\""  # Using escape characters to use both types of strings
#
# hi = "Hello World!"
# print(hi[0])  # Python starts counting at 0
# print(hi[-1])  # Returns last character in a list
# print(hi[3:8])  # Non-inclusive of the final position. Returns all characters from the first value to the second
# print(len(hi))  # returns the length of the string

# String Methods
#
# white_space = ".........lots of white space.........."
# print(len(white_space))
# print(white_space.strip())  # remove spaces (by default) or specified chars from either ends of the string
# print(white_space.upper())
# print(white_space.strip(".").capitalize())  # chained methods (separate on multiple lines)
# print(white_space.strip().count(" "))  # counts specified character
# print(white_space.replace(".", "-"))  # replaces the specified character(1st) with the chosen character(2nd)

# F-Strings (formatted strings)

# pi = 3.14159265359
# print(pi)
# print(f"Pi to 2 digital pieces: {pi:.2f}")  # prints the number plus the specified number of characters after the "."
# print(f"Pi to 5 digital pieces: {pi:.5f}")
# print(f"Pi to 0 digital pieces: {pi:.0f}")
#
# score = 16
# max_score = 26
#
# print(f"You scored {score / max_score}")
# print(f"You scored {score / max_score:.2%}")
# print(f"You scored {score / max_score:.2f}")
# print(f"You scored {score / max_score:%}")
# print(f"You scored {score / max_score:.0%}")

# Boolean
#
# t = True
# f = False
#
# print(t, type(t))
#
# print(3 + 2 == 5)
# print(12 % 3 == 0)
# print(3 != 5)
# print(1 < 100)
# print(1 > 100)
# print(5 <= 5)
# print(5 < 5)
#
# age = 19
# drink = 'alcohol'
#
# print(age > 18 and drink == 'alcohol')

# hi = 'Hello World'
#
#
# print(hi.replace(" ", "").isalpha())  # if there are only letters in the string it will return true
# print(hi.isalnum())  # if there are only letters and numbers (alphanumeric characters) in the string it will return true
# print(hi.lower().islower())  # checks if the string is all in lowercase
# print(hi.upper().isupper())  # checks if the string is all in uppercase
# print(hi.endswith("d"))  # checks if the string ends with the chosen character
# print(hi.startswith("H"))  # checks if the string ends with the chosen character

# print(bool(1))
# print(bool(0))
#
# print(int(False))
# print(int(True))
#
# empty = ""
#
# print(empty, type(empty), bool(empty))

# None type
# usable as placeholder for example

n = None

print(n, type(n))
print(bool(None))  # returns false

print(n is None)  # returns true
# "is" special work used to check types for example. Eg: print(type(15) is int)

