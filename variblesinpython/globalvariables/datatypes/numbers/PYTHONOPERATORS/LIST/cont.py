# Python - Change List Items

# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"  # Changing the second item ('banana') to 'blackcurrant'
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values.

# Example: Change 'banana' and 'cherry' with 'blackcurrant' and 'watermelon':
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # Replacing 'banana' and 'cherry'
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly.
# Example: Replace the second value with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]  # Replacing 'banana' with two new values
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']

# If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly.
# Example: Replace the second and third value with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]  # Replacing 'banana' and 'cherry' with 'watermelon'
print(thislist)  # Output: ['apple', 'watermelon']

# Insert Items
# To insert a new list item, without replacing any of the existing values, use the insert() method.
# The insert() method inserts an item at the specified index.
# Example: Insert 'watermelon' as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")  # Insert 'watermelon' at index 2
print(thislist)  # Output: ['apple', 'banana', 'watermelon', 'cherry']
