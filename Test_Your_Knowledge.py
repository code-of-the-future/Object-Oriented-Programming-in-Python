# Can you create a vehicle class using Object Oriented Programming
# Include in your initializer the colour of the car, how old
# the car is and how many seats this car has

class Vehicle:

    def __init__(self, colour_of_car, age_of_car, seats_in_car):
        self.colour_ = colour_of_car
        self.age_ = age_of_car
        self.seats_ = seats_in_car

    def colour(self):
        return "The colour of the car is {}".format(self.colour_)

    def age(self):
        return "The age of the car is {}".format(self.age_)

    def seats(self):
        return "There are {} seats in the car".format(self.seats_)

    def car_life_left(self):
        return "This car has {} years left on the road!".format(50 - self.age_)


Car = Vehicle("red", 30, 4)
print(Car.car_life_left())
print(Car.seats())
print(Car.colour())