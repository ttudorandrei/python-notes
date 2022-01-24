# A script that will ask 3 questions
# use the stored variables and print out a response
# Can you ask q with numerical answers?

name = input("What is your name?\n")
age = int(input("How old are you?\n"))  # Convert input value to integer
location = input("Where are you located?\n")

print(type(age))  # get type of value
# print("Hi, " + name + "! Wow, " + age + " that's nice! I love " + location + " it's a super nice city!")
# print("Hi, " + name + "! Wow, next year you'll be " + str(int(age) + 1) + "! That's nice! I love " + location + " it's a super nice city!")
print(f"Next year you will be {age + 1} years old")  # formatted string
