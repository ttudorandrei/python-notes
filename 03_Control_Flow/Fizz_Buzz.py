# user input for min and max number
min_number = int(input("Please choose a minimum number\n"))
max_number = int(input("Please choose a maximum number\n"))

# user input for alternate words
fizz_alt_word = input("Choose an alternate word for 'Fizz'\n")
buzz_alt_word = input("Choose an alternate word for 'Buzz'\n")

# checks every number in range if divisible with 3, 5 and prints the appropriate value
for number in range(min_number, max_number + 1):
    if (number % 5) == 0 and (number % 3) == 0:
        print(fizz_alt_word + buzz_alt_word)
    elif (number % 3) == 0:
        print(fizz_alt_word)
    elif (number % 5) == 0:
        print(buzz_alt_word)
    else:
        print(number)
