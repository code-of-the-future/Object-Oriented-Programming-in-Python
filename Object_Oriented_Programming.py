# OOP in Python!

# Every value in Python is actually considered an object!
number = 9375872
word = "hello"
# number is an object of the class 'int' and word is an object
# of the class 'str'
print(type(number), type(word))

# We can also find the type of a function!


def my_name():
    print("Ellie")


print(type(my_name))

# WE CAN CREATE OUR OWN CLASSES!!! How cool is that!!

# Every time you create something in Python you are creating
# an object that belongs to a class! This class defines the
# things that the specific object can do.

# Specifically, an object has a STATE and a collection of
# METHODS it can do/perform. The state is the things the object
# knows about itself!

# Example - using turtle
import turtle

# The turtle's postion, colour, etc is the STATE:
# turtle.color("red")  # This is the state
# The turtle's movements - forward, backwards, left, right are
# the methods!
# turtle.forward(100)  # This is the method

# We can create our very own class with methods!

# Within this class we can define the methods/operations
# that our class will do. A method is just a function
# that goes inside our class (essentially)


class Dog:

    def colour(self):
        return "brown"

# Now we can create a variable of our class, Dog!
x = Dog()
print(x)
# The '__main__' is the module that the class was defined in
# this is set by default to main

# We have created our very first class!!

# Now we can explore something known as the initializer.
# This is something EVERY class should have! It essentially
# sets the default parameters for our class. So it's similar
# to how a turtle has its own default settings.

# We will set up a new class to demonstrate the initializer!

class Dogs:

    def __init__(self):
        self.Labrador = "barnie"
        self.Poodle = 3

# Define a variable of this class - creates an instance of the
# class
a = Dogs()
# Showing our method in action!
print(a.Labrador)
print(a.Poodle)
# Two instances of the class are not always the same
b = Dogs()
print(a == b)  # This is false!

# Let's look at the extra features you can add!

class Animals:

    # initializer
    def __init__(self, animal_type, animal_age, animal_name):
        self.type = animal_type
        self.age = animal_age
        self.name = animal_name

    def type_of_animal(self):
        return 'This animal is a {}'.format(self.type)

    def age_of_animal(self):
        return 'The age is {}'.format(self.age)

    def name_of_animal(self):
        return 'The name of the animal is {}'.format(self.name)

    # You can also do some abstract things!
    def number(self):
        return self.age + 100


# Create a new variable
# It's important to add the specific parameters!
c = Animals("dog", 10, "barnie")
d = Animals("cat", 9, "muffin")
print(c.type_of_animal())
print(c.name_of_animal())
print(d.age_of_animal())
print(d.number())
