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


fido = Dog()
print(fido, type(fido))

print(fido.animal_kind)
print(fido.bark())
print(fido.bark_again(3))
print(fido.who_am_i())
print(fido.loud_bark())


class Cat:

    animal_kind = "Feline"

    def meow(self):
        return "Meow!"

    def loud_meow(self):
        return self.meow().upper()

    def who_am_i(self):
        return f"Meow, I am a {self.animal_kind}"

    def meow_repeatedly(self, number_of_meows: int):
        return "Meow! " * number_of_meows


garfield = Cat()

print(garfield.meow())
print(garfield.loud_meow())
print(garfield.who_am_i())
print(garfield.meow_repeatedly(6))

# instantiation - i.e. creating an INSTANCE of a class
tom = Cat()
schumi = Cat()

print(schumi.animal_kind)
Cat.animal_kind = "FELINE"
print(schumi.animal_kind)



