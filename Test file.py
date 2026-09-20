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

# Loops

# For loop using rang()
for i in range(5):
    print(f"The number is {i}") # Prints: The number is 0, The number is 1, ..., The number is 4

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

for name in names:
    print(f"Hello, {name}!") # Prints: Hello, Alice!, Hello, Bob!, ..., Hello, Eve!

list_of_colours = ['Red', 'Green', 'Blue', 'Yellow']
for colour in list_of_colours:
    if colour == 'Green':
        print('Green is my favourite colour!')
    else:
        print('{} is a nice colour.'.format(colour))

'''
Output:
Red is a nice colour.
Green is my favourite colour!
Blue is a nice colour.
Yellow is a nice colour.
'''

# Accessing index and value in a list using enumerate()
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(f"Item {i}: {fruit}")

'''
Output:
Item 0: apple
Item 1: banana
Item 2: cherry
'''

# more advanced for loop using range()
for i in range(0, 10, 2): # Start (inclusive), stop (exclusive), step
    print(f"The number is: {i}")

'''
output:
The number is: 0
The number is: 2
The number is: 4
The number is: 6
The number is: 8
'''

'''
Exercise 1: Finding factors using a for loop
Use a for loop to find all of the factors of 120 (i.e. all numbers n such that 120/n is an integer). 
Note that we can use the mod operator to find factors, since if m is a factor of n, then n % m is zero. 
You should loop from 1 to 120 and use an if condition within the loop to determine if each number is a factor of 120, 
and if it is, append it to a list called factors.
'''

factors = []

for i in range(1, 121):
    if 120 % i == 0:
        factors.append(i)

print(factors) # Prints: [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]


# Looping through dictionaries
student_grades = {'Connor': 85, 'Alice': 92, 'Bob': 78}

for i in student_grades:
    print(i) # prints Connor, Alice, Bob because iterating through a dictionary by default iterates through its keys

for i in student_grades.values():
    print(i) # prints 85, 92, 78 because iterating through the values of the dictionary

# Using .items() to access both values and keys in the dictionary
for student, grade in student_grades.items():
    print(f"{student}: {grade}") # prints Connor: 85, Alice: 92, Bob: 78


people_and_places = {
    'John': {'home': 'Leeds', 'born': 'Paris', 'parents': 'Paris'},
    'Fred': {'home': 'Barcelona', 'born': 'Madrid', 'parents': 'Oviedo'},
    'George': {'home': 'London', 'born': 'Bristol', 'parents': 'Exeter'},
}
info_string = '{} lives in {}. He was born in {} and his parents live in {}.'
for name, homes in people_and_places.items():
    # name and homes refer to the key and value of this dictionary item
    print(info_string.format(name, homes['home'], homes['born'], homes['parents']))

'''
Output:
John lives in Leeds. He was born in Paris and his parents live in Paris.
Fred lives in Barcelona. He was born in Madrid and his parents live in Oviedo.
George lives in London. He was born in Bristol and his parents live in Exeter.
'''

# While loop
i = 1
while i < 6:
    print(f"The number is {i}")
    i += 1 # Increment i by 1 in each iteration

'''
Output:
The number is 1
The number is 2
The number is 3
The number is 4
The number is 5
'''

'''
The following starter code sets the value of two integers, a and b. 
Write a while loop that while b>0 sets the value of the temporary variable t to b, 
then sets the value of b to a % b, and finally, sets the value of a to t.
'''
a=35
b=10
while b > 0:
    t= b
    b= a % b
    a= t
print(a) # Prints the greatest common divisor (GCD) of 35 and 10, which is 5

# Using break to exit a loop early
i = 1
while i < 10:
    print(f"The number is {i}")
    if i == 5:
        break
    i += 1

'''
Output:
The number is 1
The number is 2
The number is 3
The number is 4
The number is 5
'''

# using continue to skip the rest of the loop iteration and move to the next iteration
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(f"The number is {i}")

'''
Output:
The number is 1
The number is 3
The number is 5
The number is 7
The number is 9
'''

# Nested loops and if statements
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print(f"i and j are equal: {i}")
        else:
            print(f"i and j are not equal: i={i}, j={j}")

'''
Output:
i and j are equal: 1
i and j are not equal: i=1, j=2
i and j are not equal: i=1, j=3
i and j are not equal: i=2, j=1
i and j are equal: 2
i and j are not equal: i=2, j=3
i and j are not equal: i=3, j=1
i and j are not equal: i=3, j=2
i and j are equal: 3
'''

# List comprehensions
doubles = [i * 2 for i in range(1, 11)]
print(doubles) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension with a condition
odds = [i for i in range(1, 11) if i % 2 != 0]
print(odds) # Output: [1, 3, 5, 7, 9]

grades = {
    "Asterix" : 57,
    "Galois" : 99,
    "Cazzgr" : 45,
    "Dilbert" : 3,
}

top_students=[key for (key, value) in grades.items() if value > 50]
print(top_students) # Output: ['Asterix', 'Galois']

# If else in a list comprehension
pass_fail = ["Pass" if value >= 50 else "Fail" for value in grades.values()]
print(pass_fail) # Output: ['Pass', 'Pass', 'Fail', 'Fail']

# Filtering a list to include only integers
list_of_numbers = [3.0, 3, 7.5, 109, 2.2]
filtered = [i for i in list_of_numbers if isinstance(i, int)]
print(filtered) # Output: [3, 109]

# Functions: defining reusable blocks of code that can be called with different arguments.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Output: Hello, Alice!
greet("Bob") # Output: Hello, Bob!

def add(a,b):
    return a + b 

print(add(3, 5)) # Output: 8
print(add(10, 20)) # Output: 30

# print vs return: print displays the result immediately, while return sends the result back to the caller.

# keyword arguments: allowing you to specify arguments by name when calling a function.
def greet_with_prefix(name, prefix="Hello"):
    print(f"{prefix}, {name}!")

greet_with_prefix("Alice") # Output: Hello, Alice!
greet_with_prefix("Bob", prefix="Hi") # Output: Hi, Bob!

# define a function with two parameters - nothing is output at this stage
def isItChristmas(month, day):
    if month == 12 and day == 25:
        print('Happy Christmas')
    else:
        print('Have a nice day')
isItChristmas(12, 25) # Output: Happy Christmas
isItChristmas(11, 5) # Output: Have a nice day

# Exercise 2: Filtering words with a function
# Define a function that takes as input a list of words and returns all the words from that list that are more than 6 letters long and start with a letter that comes after ‘l’ in the alphabet (i.e. ‘m’ or later)
def filter_words(words):
    return [word for word in words if len(word) > 6 and word[0].lower() > 'l']

# Example usage:
words = ["magnificent", "apple", "zebra", "lighthouse", "mountain", "elephant"]
filtered_words = filter_words(words)
print(filtered_words) # Output: ['magnificent', 'mountain']

# Keyword arguments in any order
def isItChristmas(month, day):
    return month == 12 and day == 25

isItChristmas(day=25, month=12) # Output: True

# Optional arguments with default values
def greet_with_optional_prefix(name, prefix="Hello"):
    print(f"{prefix}, {name}!")

greet_with_optional_prefix("Alice") # Output: Hello, Alice!
greet_with_optional_prefix("Bob", prefix="Hi") # Output: Hi, Bob!

# Variable number of arguments: allowing a function to accept any number of positional arguments.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3)) # Output: 6
print(sum_all(4, 5, 6, 7)) # Output: 22

# **kwargs: allowing a function to accept any number of keyword arguments.

def print_all(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_all(name="Alice", age=30) 
# Output:
# name: Alice
# age: 30

# Variable number of positional arguments with a separator: allowing a function to accept any number of positional arguments and join them with a specified separator.
def join_strings(*args, sep=' '):
    return sep.join(args)

print(join_strings('fish', 'chips'))
print(join_strings('fish', 'chips', sep=' & '))
# Output:
# fish chips
# fish & chips

'''
Docstrings: a way to document your functions, classes, and modules in Python. 
They are written as multi-line strings (triple quotes) and are placed immediately after the definition of a function, class, or module.

def example_function(param1, param2):
    """
    This is an example function that demonstrates the use of a docstring.

    Parameters:
    param1 (int): The first parameter.
    param2 (int): The second parameter.

    Returns:
    int: The sum of param1 and param2.
    """
    return param1 + param2
'''

