print("\nQ1a\n")


# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class Country:
    def __init__(self, country_name, continent, climate, language):
        self.country_name = country_name
        self.continent = continent
        self.climate = climate
        self.language = language

    def get_continent(self):
        print(f"The country {self.country_name} is located on is {self.continent}")

    def get_climate(self):
        print(f"The climate in {self.country_name} is {self.climate}")

    def get_language(self):
        print(f"In {self.country_name} the spoken language is {self.language}")


uk = Country("United Kingdom", "Europe", "Temperate", "English")
print(uk.continent)

print("\nQ1b\n")


# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class City(Country):
    def __init__(self, country_name, continent, climate, language, city_name):
        super().__init__(country_name, continent, climate, language)
        self.city_name = city_name

    def get_city_name(self):
        print(f"This is {self.city_name} city")


london = City("United Kingdom", "Europe", "Temperate", "English", "London")

print(london.continent)
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:

list_of_primes = []
for i in list_of_numbers:
    if Number(i).is_prime():
        list_of_primes.append(i)

print(list_of_primes)

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
list_of_divisibles = []

for i in list_of_numbers:
    if Number(i).divisible_by_n(3) or Number(i).divisible_by_n(4):
        list_of_divisibles.append(i)

print(list_of_divisibles)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:

good_boss = GoodBoss("peter", "friendly", "calm", "nice")

print(good_boss.get_attitude())
print(good_boss.get_behaviour())
print(good_boss.get_face())
print(good_boss.encourage())

# -------------------------------------------------------------------------------------- #
