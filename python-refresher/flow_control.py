# Python if Statement
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

# Python if...else Statement    
number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')

#  Python if...elif...else Statement
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

# Python Nested if Statement
number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive


########## Python For Loops ###########

languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)

# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)

##### Python While Loop ####
# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number  # total = total + number

    # take integer input again
    number = int(input('Enter a number: '))

print('total =', total)

######## Python break and continue ############
for i in range(5):
    if i == 3:
        break
    print(i)

# program to find first 5 multiples of 6

i = 1

while i <= 10:
    print('6 * ', (i), '=', 6 * i)

    if i >= 5:
        break

    i = i + 1

# python continue statement
for i in range(5):
    if i == 3:
        continue
    print(i)

# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1

    if (num % 2) == 0:
        continue

    print(num)

# Python pass Statement    
n = 10

# use pass inside if statement
if n > 10:
    pass

print('Hello')
