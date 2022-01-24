# user input for min and max number
min_number = input("Please choose a minimum number\n")
max_number = input("Please choose a maximum number\n")

# user input for alternate words
fizz_alt_word = input("Choose an alternate word for 'Fizz'\n")
buzz_alt_word = input("Choose an alternate word for 'Buzz'\n")

if min_number.isnumeric() and max_number.isnumeric():
    # checks every number in range if divisible with 3, 5 and prints the appropriate value
    for number in range(int(min_number), int(max_number) + 1):
        if (number % 5) == 0 and (number % 3) == 0:
            print(fizz_alt_word + buzz_alt_word)
        elif (number % 3) == 0:
            print(fizz_alt_word)
        elif (number % 5) == 0:
            print(buzz_alt_word)
        else:
            print(number)
else:
    print("Opps! Please choose a number!")
