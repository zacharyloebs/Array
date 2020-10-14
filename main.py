# This program demonstrates how the array data structure works in Python

# O(n) complexity
# Space O(n)
# Insert O(n)
# Get Item O(1)
# Set Item O(1)
# Delete Item O(n)
# Iterate O(n)


# An array holds elements in a specific order
# Arrays are mutable meaning items can be added or removed after creation
numbers = [5, 8, 4, 12, 27, 16, 7]

# Print the contents of an array
print(numbers)

# Find the length of an array
print(len(numbers))

# Access specific elements of an array
# Prints the first element of the array
print(numbers[0])

# Change an element in the array
numbers[0] = 11
# The first element [0] has now been changed
print(numbers[0])

# Add an element to the end of the array
numbers.append(30)
# The array now has a new element at the end
print(numbers)

# Delete an a element in the array (1st method)
numbers.pop(1)
# The element in the 2nd position in the array is removed
print(numbers)

# Delete an a element in the array (2nd method)
numbers.remove(4)
# The element with a value of 4 is removed
print(numbers)
