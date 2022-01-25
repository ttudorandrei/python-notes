# i = 1
# keep_looping = True
#
# while keep_looping:
#     print(i)
#     if i == 5:
#         print("Five Party!")
#         keep_looping = False
#         # break  # will break you out from the nearest loop
#     i += 2
#
# print("Loop finished")

# break from multiple loops
# for x in ['a', 'b', 'c', 'd']:
#     break_for = False
#     i = 100
#     while i < 110:
#         print(x, i)
#         if x == 'b' and i == 105:
#             break_for = True
#             break
#         i += 1
#     if break_for:
#         break

# run input while variable is true
prompt_user = True
age = None
max_age = 119
while prompt_user:
    age = input('What is your age?\n')
    if age.isdigit():
        if int(age) <= 119:
            prompt_user = False
        else:
            print("You are not that old!")
    else:
        print("Please provide again in digits!")

print(f"Double your age is {int(age) * 2}")

