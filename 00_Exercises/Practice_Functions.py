print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:


def return_divisors(num: int):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


print(return_divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:


def is_factor(num1: int, num2: int):
    if num1 % num2 == 0:
        print("true")
    else:
        print("false")


is_factor(3, 9)
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:


def find_letter_index(letter: str):
    if letter.isalpha():
        return alphabet.index(letter.lower())
    else:
        return "Please input a letter"


print(f"The index for the letter you chose is: {find_letter_index('o')}")

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:


def name_to_id(name: str):
    output_id = ""
    if all(char.isalpha() or char.isspace() for char in name):
        for letter in name:
            output_id += str(alphabet.index(letter.lower()))
    else:
        return "Please input a name"
    return output_id


print(name_to_id("tudor"))

# 1920314172619142013

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


def id_to_password(callback):
    total_id_value = 0
    for character_value in callback:
        total_id_value += int(character_value)
    print(f"We subtract {total_id_value} from {callback}\n")
    return f"Your generated ID is {int(callback) - total_id_value}"


print(id_to_password(name_to_id("tudor")))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:




print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


def is_prime(num: int):
    try:
        for n in range(2, int(int(num) ** 1 / 2) + 1):
            if int(num) % n == 0:
                return False
        return True
    except ValueError:
        return "Please input a number"


print(is_prime("121"))


# -------------------------------------------------------------------------------------- #