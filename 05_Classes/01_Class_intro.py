# OOP - Object Oriented Programming

# we use capital letters for classes and no underscores. kind of camel case but with first letter as upper as well. UpperCamelCase

# "self" is referring to the current class
# first arg is the class itself

class Dog:
    # class variables are really dangerous
    animal_kind = "canine"  # class variable

    def bark(self):  # method
        return "Woof!"

    def bark_again(self, number_of_barks):  # method that accepts parameters
        return "Woof!" * number_of_barks

    def who_am_i(self):  # method plus personal class variable
        return f"Woof, I am a {self.animal_kind}"

    def loud_bark(self):
        return self.bark().upper()


# fido = Dog()
# print(fido, type(fido))
#
# print(fido.animal_kind)
# print(fido.bark())
# print(fido.bark_again(3))
# print(fido.who_am_i())
# print(fido.loud_bark())


class Cat:
    # when using this way of creating a class, the class itself won't have for example here,
    # an animal kind BUT, every INSTANCE created WILL HAVE an animal kind
    def __init__(self, breed, age, color):  # Initialisation, dunder (double underscore) init
        self.animal_kind = "Feline"
        self.legs = 4
        self.breed = breed
        self.age = age
        self.color = color

    def meow(self):
        return "Meow!"

    def loud_meow(self):
        return self.meow().upper()

    def who_am_i(self):
        return f"Meow, I am a {self.animal_kind}"

    def meow_repeatedly(self, number_of_meows: int):
        return "Meow! " * number_of_meows


garfield = Cat("Persian", 4, "orange")
schumi = Cat("Sphynx", 9, "blue")


class Car:
    # gearbox has default value
    def __init__(self, make, model, engine_size, color, transmission, gearbox="5 speed manual"):
        self.make = make
        self.model = model
        self.engine_size = engine_size
        self.color = color
        self.transmission = transmission
        self.gearbox = gearbox

    # decorator mo make pycharm happy with the method being in a class
    @staticmethod
    def rev_engine(self):
        return "Vrrruummm"

    @staticmethod
    def loud_rev(self):
        return "Vvvvrrrruuuuummmmm"


first_car = Car("Toyota", "Aristo", 3000, "black", "RWD", "6 speed automatic")
print(first_car.make, first_car.model, first_car.engine_size, first_car.color, first_car.transmission, first_car.gearbox)
