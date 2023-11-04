class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    pass


# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()


## Multilevel Interitance ##
class SuperClass:

    def super_method(self):
        print("Super Class method called")


# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")


# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"
