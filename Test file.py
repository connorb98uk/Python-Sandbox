import math

name = 'Connor'
print(f'Hello, {name}!') # Outputs: Hello, Connor!

print(math.floor(3.7))  # Outputs: 3
print(math.ceil(3.2))   # Outputs: 4
print(math.pi)        # Outputs: 3.141592653589793

# Simple operators
print(5 + 3.0) # Prints: 8.0, notice adding an int and a float results in a float

# Note that int() rounds towards zero, while // always rounds down. For positive numbers, they’re the same; for negative numbers, they differ:
print(int(-1.7)) # Prints: -1
print(int(3.7))  # Prints: 3

# Numerical Comparison
print(1 == 2) # Prints: False
print(1 != 2) # Prints: True
print(1 < 2)  # Prints: True
print(1 > 2)  # Prints: False
print(1 <= 2) # Prints: True
print(1 >= 2) # Prints: False
print(type(1 == 2)) # Prints: <class 'bool'>

# Use the comparison relations to determine whether 3⁹ is less than 113 × 152.
print(3**9) # Prints: 19683
print(113 * 152) # Prints: 17176
print(f'Therefore the answer is {3**9 < 113 * 152}') # Prints: Therefore the answer is False

# Try to determine what operations result in an int and what result in a float
print(5 + 3) # Prints: 8
print(5 + 3.0) # Prints: 8.0
print(5 * 20) # Prints: 100
print(5 * 20.0) # Prints: 100.0
print(5 / 2) # Prints: 2.5
print(5 // 2) # Prints: 2

# Strings and escape characters
print('Connor\nBlackburn') # Prints:
# Connor
# Blackburn

print('Connor\tBlackburn') # Prints: Connor	Blackburn
print('\'Connor Blackburn\'') # Prints: 'Connor Blackburn'


