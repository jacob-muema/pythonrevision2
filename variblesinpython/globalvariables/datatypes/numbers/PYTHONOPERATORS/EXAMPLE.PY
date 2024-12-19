# Python Operators

# Operators are used to perform operations on variables and values.

# Arithmetic Operators
# Used with numeric values to perform common mathematical operations:

# +: Addition
# -: Subtraction
# *: Multiplication
# /: Division
# %: Modulus (remainder of division)
# **: Exponentiation (power)
# //: Floor division (integer division, discarding remainder)

print(10 + 5)  # Example of addition

# Assignment Operators
# Used to assign values to variables:

x = 5       # Simple assignment
x += 3      # Equivalent to: x = x + 3
x -= 3      # Equivalent to: x = x - 3
x *= 3      # Equivalent to: x = x * 3
x /= 3      # Equivalent to: x = x / 3

# Comparison Operators
# Used to compare two values:

print(x == 5)  # Equal
print(x != 5)  # Not equal
print(x > 3)   # Greater than
print(x < 10)  # Less than

# Logical Operators
# Used to combine conditional statements:

print(x < 5 and x < 10)  # and (True if both are true)
print(x < 5 or x > 10)   # or (True if one is true)
print(not(x < 5))        # not (inverts the result)

# Identity Operators
# Compare if two objects are the same (memory location):

y = [1, 2]
z = y
print(y is z)       # True if y and z are the same object
print(y is not z)   # False if y and z are the same object

# Membership Operators
# Check if a value exists in a sequence:

print(1 in y)    # True if 1 exists in y
print(3 not in y)  # True if 3 does not exist in y

# Bitwise Operators
# Perform operations on the binary representation of numbers:

x = 6  # 110 in binary
y = 3  # 011 in binary

print(x & y)  # AND (binary comparison)
print(x | y)  # OR (binary comparison)
print(x ^ y)  # XOR (binary comparison)
print(~x)     # NOT (inverts the bits)
print(x << 2) # Left shift (shifts bits left)
print(x >> 2) # Right shift (shifts bits right)

# Operator Precedence
# Describes the order in which operations are performed:

# Parentheses () have the highest precedence
print((6 + 3) - (6 + 3))

# Multiplication * has higher precedence than addition +
print(100 + 5 * 3)  # Evaluates as: 100 + (5 * 3)

# Operators with the same precedence are evaluated left to right:
print(5 + 4 - 7 + 3)  # Evaluates as: ((5 + 4) - 7) + 3 = 5
