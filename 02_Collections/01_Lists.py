# Lists

# shopping_list = ["eggs", "bread", "bananas", "tea"]
#
# print(shopping_list, type(shopping_list))
# print(len(shopping_list))  # returns the length of the list
#
# print(shopping_list[0])  # returns first idem in list
# print(shopping_list[-1])  # returns last item in list
#
# shopping_list[2] = "milk"  # replaces value with given value (reassigns a new value to index)
# print(shopping_list)
# # shopping_list[4] = "biscuits"  # not going to work, out of range
# shopping_list.append("biscuits")  # changes the list, adds an item at the end of it. doesn't return, only executes
#
# shopping_list.append("bread")
# print(shopping_list)
#
# shopping_list.remove("bread")  # removes specified value
# print(shopping_list)
#
# shopping_list.pop()
# # removes the value based on the position (accepts an index). changes the list and returns the removed item
# print(shopping_list)

# mixed = [1, 2, "three", True, None, False, ["another", "list"]]
# print(mixed)
#
# mixed[1] = 2.0
# print(mixed)
#
# # LIST ARE MUTABLE
#
# print(mixed[2:4])  # everything in between
# print(mixed[:6])  # all from start to specified index (goes the other way around as well)
# print(mixed[7:0:-1])  # returns the list from end to start
# print(mixed[::3])  # returns the list items in steps of three
# print(mixed[6][0][0])  # returns the first char in first item in the 7th item in the mixed list

# sublist = mixed[6].copy()
# print(sublist)
# sublist[0] = "a"
# print(mixed)
# print(sublist)

# Tuples. IMMUTABLE. Use in place of list when you want strict immutability

# colours = ("red", "blue", "green")
# print(colours, type(colours))
#
# print(colours[0])
# # this is going to fail, tuples are immutable
# # colours[0] = "maroon"
# # print(colours[0])
#
# # counts occurrences of given value in tuple
# print(colours.count("red"))
#
# list_in_tuple = (
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# )
#
# list_in_tuple[0][-1] = 2
#
# print(list_in_tuple)


