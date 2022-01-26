# pass things between functions

x = 1
y = 2
print(x, y)


# if you return multiple values you can assign them to other variables when calling the function. e.g.:
def local_scope():
    a = 500
    b = 700
    return a, b


x, y = local_scope()
print(x, y)
