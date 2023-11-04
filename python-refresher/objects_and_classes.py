## Python Class and Objects ##
# define a class
class Bike:
    name = ""
    gear = 0


# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


## Methods ##
# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the attributes 
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()


## Constructors ##
class Bike:

    # constructor function    
    def __init__(self, name=""):
        self.name = name


bike1 = Bike()
