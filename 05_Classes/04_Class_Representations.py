# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     # representation. when you print the class, it shows what you tell it in the __repr__ method.
#     # good repr looks like source code
#     def __repr__(self):
#         return f"Location(latitude={self.latitude}, longitude={self.longitude})"
#
#     # string representation
#     # designed to display readable human information.
#     # if there is no string, it will show the __repr__
#     def __str__(self):
#         return f"({self.latitude}, {self.longitude})"
#
#
# bham_academy = Location(52.488647, -1.887249)
#
# print(repr(bham_academy))
# print(bham_academy)
# print(f"The Sparta Global Academy is located at coordinates {bham_academy}")


class Dog:
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return f"Dog(age={self.age})"

    def __str__(self):
        return f"A {self.age} years old dog"

    # return a formatted string if a format spec is provided. otherwise, it will just return the __str__() result
    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"{self.age * 7} dog-years old dog"
        else:
            return self.__str__()

fido = Dog(5)
print(fido)
print(f"Fido is a {fido:dog}")



