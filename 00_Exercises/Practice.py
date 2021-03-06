print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for item in x:
    if item % 2 == 0:
        print(item)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for item in x[:5]:
    if item % 2 == 0:
        print(item)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
new_list = []
for item in names:
    new_list.append(item[0])

print(new_list)



print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
new_list = []
for item in names:
    new_list.append(item.index(" "))

print(new_list)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
new_list = []
for item in names:
    # slices the first and last chars for each string
    new_list.append(item[::len(item)-1])

print(new_list)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates

list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

for item in list_of_lists:
    if len(item) == len(set(item)):
        print(item)

# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
prompt_user = True
while prompt_user:
    user_input_num = input("Please input a number!\n")
    if user_input_num.isdigit():
        if int(user_input_num) > 100:
            prompt_user = False
            for n in range(2, int(int(user_input_num) / 2) + 1):
                if int(user_input_num) % n == 0:
                    print(f"{user_input_num} is not a prime number.")
                    break
                else:
                    print(f"{user_input_num} is a prime number.")
            print(user_input_num)
        else:
            print("Your number has to be greater than 100!\n")

    else:
        print("Oops! Please provide again in digits\n")


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
