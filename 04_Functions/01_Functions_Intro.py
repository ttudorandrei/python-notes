# TODO: look into qwargs


# define functions using "def"
# def woof(number_of_woofs):
#     for i in range(number_of_woofs):
#         print("Woof")
#
#
# def meow(no_of_meows):
#     print("Meow!" * no_of_meows)
#
#
# woof(13)
# meow(12)


# def double_plus_num(num1, num2):
#     answer = (num1 * 2) + num2
#     return answer


# x = double_plus_num(248, 356)
# print(double_plus_num(34576, 8453))
# print(x, x, x)


# choose default value for the second argument. all default arguments must come after non default arguments
# def double_plus_num_default(num1, num2=1):
#     answer = (num1 * 2) + num2
#     return answer

# multiple arguments
# CAN hold default arguments
# def shopping(name, *items, shout=False):
#     if shout:
#         name = name.upper()
#     for item in items:
#         print(f"{name}! Don't forget to buy a {item}")


# when multiple args with default ones, specify the name when changing the value of the default argument
# shopping("Tudor", "banana", "bottle of milk", "orange", shout=True)

# Type Hints
# def greeting(name: str = "Tudor"):
#     print(f"Hello to you, {name}")
#     # print("Hello to you, " + {name})
#
#
# # the "-> int" is a type hint for the output
# def double_plus_num(num1: int, num2: int) -> int:
#     ans = (num1 * 2) + num2
#     return ans

# Best practices
"""
Name with lowercase and underscores
better to have longer but explicit names rather than short undescriptive ones
always return (otherwise it'll return none by default)
keep functions small. when too big, break it into multiple smaller functions
"""

