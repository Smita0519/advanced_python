# Variables and Input:
# 1. Create a variable my_age and assign your age to it. Print a message using this variable.

my_age = 20
print(my_age)

""" 
output: 
20 
"""

# 2. Ask the user to enter their favorite food and print a message incorporating this input.

fav_food = input("enter your favourite food: ")
print("favourite food: ",fav_food)

""" 
output:enter your favourite food: apple
favourite food:  apple 
"""

# Type Conversion:
# 1. Convert the string "42" to an integer and print the result.

st = "42"
print("the integer is",int(st))

"""
output:
the integer is 42
"""

# 2. Convert the floating-point number 3.14159 to a string and print the result.

fl = 3.14159
print("the string is",str(fl))

"""
output:
the string is 3.14159
"""

# Strings:
# 1. Concatenate the strings "Hello" and "World!" and print the result.

s1 = 'Hello'
s2 = ' World'
print("the concatenated string is", s1+s2)

"""
output:
the concatenated string is Hello World
"""

# 2. Use string indexing to extract the third character from the string "Python".

str = "Python"
print(str[2])

"""
output:
t
"""

# 3. Take a sentence as input and print only the first five words.

strs = "Life is a winking light in the darkness."
words = strs.split()
first_five_words = words[:5]
result = " ".join(first_five_words)
print(result)

first_five = ' '.join(strs.split()[:5])
print(first_five)

"""
output:
Life is a winking light
Life is a winking light
"""