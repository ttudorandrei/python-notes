# Inheritance and Polymorphism


class Mammal:
    def __init__(self, name):
        self.warm_blood = True
        self.name = name

    def reproduce(self):
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True
        # self.warm_blood = False

    def reproduce(self):
        print("laying eggs")

"""
To Inherit, pass in the parent class as a param when creating the child class
"""
# when we create a class that inherits from another class, we need to run super().__init__()
# to not overwrite the super init method


class Horse(Mammal):
    def __init__(self, name, jockey):
        # init needs an argument because the Mammal class expects an argument
        super().__init__(name)
        self.legs = 4
        self.jockey = jockey

    def pregnancy(self):
        print("Wait 11 months")
        # super lets us refer to the parent class
        super().reproduce()


class Pony(Horse):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)

    def give_birth(self):
        super().reproduce()


"""
If there is a method that is being overwritten on a child class, a second child class would only have access to the
overwritten method
"""

# perry = Platypus("perry")
# print(perry.poisonous_barbs)
# print(perry.reproduce())


# m = Mammal("Charlie")
# h = Horse("Horsey", "name of jockey")
# print(h.warm_blood)
# print(h.reproduce())
# print(h.name)
# print(h.jockey)
# print("---------------------------")
# p = Pony("My little Pony")
# print(p.legs)
# p.pregnancy()
# p.give_birth()

