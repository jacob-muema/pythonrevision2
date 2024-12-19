# Accessing List Items

# Lists are indexed, so you can access elements by referring to their index number.
thislist = ["apple", "banana", "cherry"]

# Example: Accessing the second item (index 1)
print(thislist[1])  # Outputs: 'banana'

# Note: The first item has an index of 0.

# Negative Indexing
# Negative indexing starts from the end of the list.
# Example: Access the last item
print(thislist[-1])  # Outputs: 'cherry'

# Range of Indexes
# You can specify a range by providing the start and end index.
# The end index is not included in the result.

# Example: Accessing items from index 2 to 4 (third to fifth item)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Outputs: ['cherry', 'orange', 'kiwi']

# If you leave out the start value, the range starts from the beginning of the list.
# Example: Get items from the start to index 3 (but not including index 4)
print(thislist[:4])  # Outputs: ['apple', 'banana', 'cherry', 'orange']

# If you leave out the end value, the range goes to the end of the list.
# Example: Get items from index 2 to the end
print(thislist[2:])  # Outputs: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes
# You can use negative indexing in ranges too.

# Example: Get items from "orange" (-4) to "kiwi" (-2)
print(thislist[-4:-1])  # Outputs: ['orange', 'kiwi', 'melon']

# Check if an item exists in the list
# Use the 'in' keyword to check for the presence of an item.

# Example: Check if "apple" is in the list
if "apple" in thislist:
    print("Yes, 'apple' is in the list.")  # Outputs: Yes, 'apple' is in the list.
