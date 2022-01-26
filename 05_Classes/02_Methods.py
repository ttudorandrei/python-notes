class Car:
    def __init__(self, current_speed=0, max_speed=0):
        # _current_speed is a protected variable due to the "_" before the actual name
        # __current_speed is impenetrable because of the "__" before the actual var name. It can not be edited
        # self._current_speed = current_speed
        self.__current_speed = current_speed
        self.max_speed = max_speed
    # setter method
    def accelerate(self, speed_increase):
        self.__current_speed += speed_increase
        if self.__current_speed > self.max_speed:
            return f"You have now reached the max speed of {self.max_speed}"
        else:
            return self.__current_speed

    def decelerate(self, speed_decrease):
        self.__current_speed -= speed_decrease
        if self.__current_speed < 0:
            return "You are now stationary"
        else:
            return self.__current_speed
    # getter method
    def get_speed(self):
        return self.__current_speed


lexus = Car(20, 150)

print(lexus.accelerate(10))
print(lexus.accelerate(10))
print(lexus.decelerate(10))
print(lexus.get_speed())
