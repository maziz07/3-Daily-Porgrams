# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing list items
print(fruits[1])  # Outputs 'banana'

# Changing the value of a list item
fruits[1] = "blueberry"

# Looping through a list
for fruit in fruits:
    print(fruit)

# List Comprehensions
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
