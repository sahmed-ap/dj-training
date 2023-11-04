def greet():
    print('Hello World!')


# call the function
greet()

print('Outside function')


# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)


# function call with two values
add_numbers(5, 4)


# Output: Sum: 9


# function definition
def find_square(num):
    result = num * num
    return result


# function call
square = find_square(3)

print('Square:', square)

# Output: Square: 9


## Python Library Function ##

import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is", square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is", power)


## Function Argument with Default Values ##

def add_numbers(a=7, b=8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a=2)

# function call with no arguments
add_numbers()


## Python Keyword Argument ##

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)


display_info(last_name='Cartman', first_name='Eric')


## Python Function With Arbitrary Arguments ##

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("Sum = ", result)


# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
