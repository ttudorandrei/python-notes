def fizz_buzz():
    # user input for min and max number
    min_number = input("Please choose a minimum number\n")
    max_number = input("Please choose a maximum number\n")

    # user input for alternate words
    fizz_alt_word = input("Choose an alternate word for 'Fizz'\n")
    buzz_alt_word = input("Choose an alternate word for 'Buzz'\n")

    def fizz_buzz_logic():
        while True:
            if min_number.isdigit() and max_number.isdigit():
                for number in range(int(min_number), int(max_number) + 1):
                    if (number % 5) == 0 and (number % 3) == 0:
                        print(fizz_alt_word + buzz_alt_word)
                    elif (number % 3) == 0:
                        print(fizz_alt_word)
                    elif (number % 5) == 0:
                        print(buzz_alt_word)
                    else:
                        print(number)
                break
            else:
                print("Oops! Please provide again in digits")
                break

    fizz_buzz_logic()


fizz_buzz()
