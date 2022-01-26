# import car_class - one way of importing. need to use the object notation to get the class
from car_class import Car, something_else  # can be used just as is

# when we import a class, all methods in that file are being run. That includes prints
# and so on

new_car = Car(0, 210)
print(new_car.accelerate(220))
print(__name__)  # "__main__"
print(something_else)
