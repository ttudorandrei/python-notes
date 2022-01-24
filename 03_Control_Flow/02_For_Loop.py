# For loops

my_list = ["a", "b", "c"]
i = 0

# for letter in my_list:
#     if letter == "b":
#         print(letter.upper())
#     else:
#         print(letter)


# for i in range(1, 10):
#     for letter in my_list:
#         print(i, letter)
#
#     i = i + 1
#     print(i)

# me = {"name": "Tudor", "age": 375, "job": "DevOps Engineer"}

# for thing in me:
#     print(thing)  # prints every key
#     print(me[thing])  # prints the value for every key

# for thing in me.values():
#     print(thing)

# for key, value in me.items():
#     print(f"My {key} is {value}")

# for index, letter in enumerate(my_list):
#     print(f"{letter} is in position {index}")

# user input for min and max number
min_number = int(input("Please choose a minimum number"))
max_number = int(input("Please choose a maximum number"))

# user input for alternate words
fizz_alt_word = input("Choose an alternative word for 'Fizz'")
buzz_alt_word = input("Choose an alternative word for 'Buzz'")


for number in range(min_number, max_number):
    if (number % 5) == 0 and (number % 3) == 0:
        print(fizz_alt_word + buzz_alt_word)
    elif (number % 3) == 0:
        print(fizz_alt_word)
    elif (number % 5) == 0:
        print(buzz_alt_word)
    else:
        print(number)
