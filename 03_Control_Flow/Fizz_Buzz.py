# user input for min and max number
min_number = int(input("Please choose a minimum number"))
max_number = int(input("Please choose a maximum number"))

# user input for alternate words
fizz_alt_word = input("Choose an alternative word for 'Fizz'")
buzz_alt_word = input("Choose an alternative word for 'Buzz'")

# checks every number in range if divisible with 3, 5 and prints the appropriate value
for number in range(min_number, max_number):
    if (number % 5) == 0 and (number % 3) == 0:
        print(fizz_alt_word + buzz_alt_word)
    elif (number % 3) == 0:
        print(fizz_alt_word)
    elif (number % 5) == 0:
        print(buzz_alt_word)
    else:
        print(number)
