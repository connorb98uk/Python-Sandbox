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


# More string operations
name = 'Connor Blackburn'
print(f'{name*2}') # Prints: Connor BlackburnConnor Blackburn
print(f'{name[0]}') # Prints: C
print(f'{name[-1]}') # Prints: n
print(f'{name[0:6]}') # Prints: Connor
print(f'{name[7:]}') # Prints: Blackburn
print(f"'Connor' in name: { 'Connor' in name }")    # Prints: True
print(f'Length of name: { len(name) }') # Prints: 15

# Using step to skip characters
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[::2]) # Prints: acegikmoqsuwy because it takes every second character
print(alphabet[1::3]) # Prints: bfjnt because it starts at index 1 and takes every third character
print(alphabet[::-1]) # Prints: zyxwvutsrqponmlkjihgfedcba because it starts at the end and goes backwards

# Exercise 2 - In Python, which is smaller, "post office" or "post-haste"?
print(f'The length of post office is {len("post office")}') # Prints: The length of post office is 11
print(f'The length of post-haste is {len("post-haste")}') # Prints: The length of post-haste is 10
print('Therefore, "post-haste" is smaller than "post office"') # Prints: Therefore, "post-haste" is smaller than "post office"

# Even more string methods
print(f"'Hello World'.startswith('Hello'): { 'Hello World'.startswith('Hello') }") # Returns: True
print(f"'Hello World'.endswith('World'): { 'Hello World'.endswith('World') }") # Returns: True

name = 'Connor Blackburn'
print(f'{name.upper()}') # Prints: CONNOR BLACKBURN
print(f'{name.lower()}') # Prints: connor blackburn
print(f'{name.title()}') # Prints: Connor Blackburn
print(f'{name.isupper()}') # Prints: False
print(f'{name.islower()}') # Prints: False

# Use split and len to count how many words there are in the sentence “You must be the change you wish to see in the world”
sentence = "You must be the change you wish to see in the world"
words = sentence.split()
print(f'There are {len(words)} words in the sentence: "{sentence}"') # Prints: There are 12 words in the sentence: "You must be the change you wish to see in the world"

# Use split and join to remove the hyphen characters in the sentence “I find the use of hyphens counter-intuitive and not straight-forward”
sentence_with_hyphens = "I find the use of hyphens counter-intuitive and not straight-forward"
sentence_without_hyphens = sentence_with_hyphens.replace('-', ' ')
print(f'Sentence without hyphens: "{sentence_without_hyphens}"') # Prints: Sentence without hyphens: "I find the use of hyphens counter intuitive and not straight forward"

# F string vs .format()
name = 'Connor'
age = 28
print(f'Hello, {name}. You are {age} years old.') # Prints: Hello, Connor. You are 28 years old.
print('Hello, {}. You are {} years old.'.format(name, age)) # Prints: Hello, Connor. You are 28 years old.

# Bools
print(3 < 2) # Prints: False
print(3 > 2) # Prints: True
print(3 == 2) # Prints: False
print(3 != 2) # Prints: True
print(True and True) # Prints: True
print(True and False) # Prints: False
print(True or False) # Prints: True
print(not True) # Prints: False

# if statements
x = 10
if x > 5:
    print(f'{x} is greater than 5') # Prints: 10 is greater than 5

# if else statements
x = 3
if x > 5:
    print(f'{x} is greater than 5')
else:
    print(f'{x} is not greater than 5') # Prints: 3 is not greater than 5

# if elif else statements
x = 5
if x > 5:
    print(f'{x} is greater than 5')
elif x == 5:
    print(f'{x} is equal to 5') # Prints: 5 is equal to 5
else:
    print(f'{x} is less than 5')

# None type - You might use None to initialise a variable before you know what its actual value should be
result = None
print(result) # Prints: None
print(type(result)) # Prints: <class 'NoneType'>

# lists
list_of_numbers = [1, 3, 7, 9, 12, 10, 2] # Prints: [1, 3, 7, 9, 12, 10, 2]
list_of_strings = ["this", "is", "a", "list"] # Prints: ["this", "is", "a", "list"]
nested_list = [ [1,2,3], [4,5,6], [7,8,9] ] # Prints: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(range(3))) # Prints: [0, 1, 2]
print(list_of_numbers[0]) # Prints: 1
print(list_of_numbers[-1]) # Prints: 2

# list slicing
print(list_of_numbers[1:4]) # Prints: [3, 7, 9] because it starts at index 1 and goes up to but not including index 4
print(list_of_numbers[:4]) # Prints: [1, 3, 7, 9] because it starts at index 0 and goes up to but not including index 4
print(list_of_numbers[4:]) # Prints: [12, 10, 2] because it starts at index 4 and goes to the end of the list
print(list_of_numbers[::2]) # Prints: [1, 7, 12, 2] because it starts at index 0 and takes every second element
print(list_of_numbers[::-1]) # Prints: [2, 10, 12, 9, 7, 3, 1] because it starts at the end of the list and goes backwards

# Nested list
list_of_lists = [[1,2,3], ['a', 'b', 'c'], ['fish', 'dog', 'cat']]
print(list_of_lists[0]) # Prints: [1, 2, 3]
print(list_of_lists[1][0]) # Prints: a
print(list_of_lists[2][1]) # Prints: dog

# Tuples - Tuples are immutable, meaning they cannot be changed after they are created. They are defined using parentheses () instead of square brackets [].
my_tuple = ('fish', 'dog', 'cat')
print(my_tuple) # Prints: ('fish', 'dog', 'cat')
print(my_tuple[1]) # Prints: dog
# my_tuple[1]='guinea pig' Trying to modify a tuple will result in an error.

# Sets - Sets are unordered collections of unique elements. They are defined using curly braces {}.
my_set = {1, 2, 3, 4, 5}
print(my_set) # Prints: {1, 2, 3, 4, 5}
my_set.add(6) # Adds 6 to the set
print(my_set) # Prints: {1, 2, 3, 4, 5, 6}
my_set.add(3) # Trying to add 3 again will not change the set because sets only contain unique elements
print(my_set) # Prints: {1, 2, 3, 4, 5, 6}
my_set.remove(4) # Removes 4 from the set
print(my_set) # Prints: {1, 2, 3, 5, 6}
print(3 in my_set) # Returns: True

# Dictionaries - Dictionaries are unordered collections of key-value pairs. They are defined using curly braces {} with colons separating keys and values.
my_dict = {'name': 'Connor', 
           'age': 28, 
           'city': 'Newcastle'}
print(my_dict) # Prints: {'name': 'Connor', 'age': 28, 'city': 'Newcastle'}
print(my_dict['name']) # Prints: Connor
my_dict['age'] = 29 # Updates the value of the key 'age' to 29
print(my_dict) # Prints: {'name': 'Connor', 'age': 29, 'city': 'Newcastle'}
my_dict['country'] = 'UK' # Adds a new key-value pair to the dictionary
print(my_dict) # Prints: {'name': 'Connor', 'age': 29, 'city': 'Newcastle', 'country': 'UK'}
del my_dict['city'] # Removes the key-value pair with the key 'city'
print(my_dict) # Prints: {'name': 'Connor', 'age': 29, 'country': 'UK'}
print('age' in my_dict) # Returns: True 

print(my_dict.keys()) # Returns: dict_keys(['name', 'age', 'country'])
print(my_dict.values()) # Returns: dict_values(['Connor', 29, 'UK'])
print(my_dict.items()) # Returns: dict_items([('name', 'Connor'), ('age', 29), ('country', 'UK')])

student_grades = {
    "Asterix": [57, 62, 59],
    "Galois": [99, 98, 100],
    "Cazzgr": [45, 52, 48]
}
print(student_grades) # Prints: {'Asterix': [57, 62, 59], 'Galois': [99, 98, 100], 'Cazzgr': [45, 52, 48]}
print(student_grades["Asterix"]) # Prints: [57, 62, 59]
print(student_grades["Asterix"][0]) # Prints: 57

# Nested dictionaries
nested_dict = {
    "Asterix": {
        "Math": 57,
        "Science": 62,
        "English": 59
    },
    "Galois": {
        "Math": 99,
        "Science": 98,
        "English": 100
    },
    "Cazzgr": {
        "Math": 45,
        "Science": 52,
        "English": 48
    }
}
print(nested_dict) # Prints: {'Asterix': {'Math': 57, 'Science': 62, 'English': 59}, 'Galois': {'Math': 99, 'Science': 98, 'English': 100}, 'Cazzgr': {'Math': 45, 'Science': 52, 'English': 48}}
print(nested_dict["Asterix"]) # Prints: {'Math': 57, 'Science': 62, 'English': 59}
print(nested_dict["Asterix"]["Math"]) # Prints: 57

# Class and Objects are the two main aspects of object-oriented programming. A class is a blueprint for creating objects, and an object is an instance of a class. Classes can have attributes (variables) and methods (functions) that define the behavior of the objects created from the class.
class Tile:
    def __init__(self, w, h, c):
        self.width = w
        self.height = h
        self.colour = c
        self.material = "ceramic"

my_tile = Tile(10, 10, "red")  # an object of class Tile
print(f'My tile is {my_tile.width}cm wide by {my_tile.height}cm high, it is {my_tile.colour} and made of {my_tile.material}.') # Prints: My tile is 10cm wide by 10cm high, it is red and made of ceramic.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3) # an object of class Dog, which means that my_dog is an instance of the Dog class. The __init__ method is called when the object is created, and it initializes the name and age attributes of the object. The bark method is a function that belongs to the Dog class, and it returns a string that includes the name of the dog and the sound it makes.
print(my_dog.bark())  # Prints: Buddy says woof!
print(f"My dog is {my_dog.age} years old.") # Prints: My dog is 3 years old.

# Try/Except - The try block lets you test a block of code for errors. The except block lets you handle the error.
try:
    print(10 / 0) # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!") # Prints: You can't divide by zero!  

try:
    print(int("hello")) # This will raise a ValueError
except ValueError:
    print("You can't convert a string to an integer!") # Prints: You can't convert a string to an integer! 


# Functions - A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def greet(name):
    return f"Hello, {name}!"
print(greet("Connor")) # Prints: Hello, Connor!

# Multiple arguments functions
def add_numbers(a, b):
    return a + b
print(add_numbers(5, 3)) # Prints: 8

# Loops - A loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string). The for loop is used to iterate over a sequence, while the while loop is used to execute a block of code as long as a condition is true.
# For loop
for i in range(5):
    print(i) # Prints: 0, 1, 2, 3, 4

# While loop
count = 0
while count < 5:
    print(count) # Prints: 0, 1, 2, 3, 4
    count += 1

# List comprehensions - A list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers) # Prints: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

doubled_numbers = [x*2 for x in range(10)]
print(doubled_numbers) # Prints: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

'''
Module 1 - Unit 2
'''

# Condition Statements - Condition statements are used to perform different actions based on different conditions. The if statement is used to test a condition, and the elif and else statements are used to test additional conditions or provide a default action.
x = 10

# If
if x > 5:
    print(f'{x} is greater than 5') # Prints: 10 is greater than 5

# Elif
if x > 5:
    print(f'{x} is greater than 5') # Prints: 10 is greater than 5
elif x == 5:
    print(f'{x} is equal to 5')
else:
    print(f'{x} is less than 5')

# More advanced elif statements with multiple conditions
if x > 5 and x < 15:
    print(f'{x} is greater than 5 and less than 15') # Prints: 10 is greater than 5 and less than 15
elif x == 5 or x == 15:
    print(f'{x} is equal to 5 or 15')

# More advanced if, elif, else statements with multiple conditions
score = 85
grade = None

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"A score of {score} receives a grade of {grade}.") # Prints: A score of 85 receives a grade of B.

# Task if statements to determine the boxer's weight division based on their weight. 
weight = math.sqrt(2622) # = 51.209
division = None

if 48 < weight <= 49:
    division = "light flyweight"
elif 49 < weight <= 51:
    division = "flyweight"
elif 51 < weight <= 52:
    division = "super flyweight"

print(f"A boxer with weight {weight:5.3f}kg is in the {division} division.") # Prints: A boxer with weight 51.209kg is in the flyweight division.

# Nested conditional 
sunny = True
temp = 12
if sunny:
    print("A beautiful sunny day. Let's go for a walk!")
    if temp < 10:
        # it's sunny AND the temperature is less than 10 degrees
        print("And we should take a good coat on our walk.")
    if temp > 20:
        # it's sunny AND the temperature is greater than 20 degrees
        print("And don't forget to pack lots of water for the walk.")

# Type conversion functions - Type conversion functions are used to convert a value from one data type to another. The int() function converts a value to an integer, the float() function converts a value to a float, and the str() function converts a value to a string.
print(int(3.7)) # Prints: 3
print(float(3)) # Prints: 3.0
print(str(3)) # Prints: '3'