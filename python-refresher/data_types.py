num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1 + 2j
print(num3, 'is of type', type(num3))

### LIST ###
languages = ["Swift", "Java", "Python"]
print(languages, 'is of type', type(languages))

# access element at index 0
print(languages[0])  # Swift

# access element at index 2
print(languages[2])  # Python

### TUPLE ###
# create a tuple 
product = ('Microsoft', 'Xbox', 499.99)

# access element at index 0
print(product[0])  # Microsoft

# access element at index 1
print(product[1])  # Xbox

print(product, 'is of type', type(product))

### SET ###
# create a set named student_id
student_id = {112, 114, 116, 118, 115}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))

print(student_id, 'is of type', type(student_id))

### DICTIONARY ###
# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)

print(capital_city['Nepal'])  # prints Kathmandu

print(capital_city, 'is of type', type(capital_city))
