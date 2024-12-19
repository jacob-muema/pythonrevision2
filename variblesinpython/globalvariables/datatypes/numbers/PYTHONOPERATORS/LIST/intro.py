# Python Lists
# Lists are used to store multiple items in a single variable.
# They are one of the 4 built-in data types in Python (along with Tuple, Set, and Dictionary).
# Lists are created using square brackets [].

# Example: Create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)  # Outputs: ['apple', 'banana', 'cherry']

# List Characteristics
# Lists are:
# - Ordered: Items have a defined order that will not change.
# - Changeable: We can add, remove, or modify items after the list has been created.
# - Allow duplicates: Lists can have multiple items with the same value.

# Example: List with duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  # Outputs: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# List Indexing
# Items in a list are indexed. The first item has index 0, the second item index 1, etc.

# Example: Access the first and second item
print(thislist[0])  # Outputs: 'apple'
print(thislist[1])  # Outputs: 'banana'

# List Length
# Use the len() function to find the number of items in a list.

# Example: Find the length of the list
print(len(thislist))  # Outputs: 5

# List Data Types
# List items can be of any data type, and a list can contain different data types.

# Example: A list with different data types
mixed_list = ["abc", 34, True, 40, "male"]
print(mixed_list)

# Check the data type of a list
print(type(mixed_list))  # Outputs: <class 'list'>

# The list() Constructor
# We can use the list() constructor to create a new list.

# Example: Using the list constructor
thislist = list(("apple", "banana", "cherry"))  # Note the double round brackets
print(thislist)  # Outputs: ['apple', 'banana', 'cherry']

# Python Collections (Arrays)
# Python has four collection data types:
# 1. List: Ordered, changeable, allows duplicates.
# 2. Tuple: Ordered, unchangeable, allows duplicates.
# 3. Set: Unordered, unchangeable, no duplicates.
# 4. Dictionary: Ordered (from Python 3.7+), changeable, no duplicate keys.

# Summary of When to Use:
# - List: Use when you need an ordered collection that can be changed and allows duplicates.
# - Tuple: Use when you need an ordered collection that does not change.
# - Set: Use when you need a collection of unique, unordered items.
# - Dictionary: Use when you need key-value pairs with unique keys.
