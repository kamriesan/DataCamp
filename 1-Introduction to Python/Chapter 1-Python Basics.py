# DataCamp Data Scientist with Python
# 1-Introduction to Python
# Chapter 1-Python Basics

# The Python Interface
print(5 / 8)
print(7 + 10)




# Any comments?
# Use hashtag




# Python as a calculator
# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)




# Variable Assignment
savings = 100
print(savings)




# Calculations with variables
savings = 100
growth_multiplier = 1.1
result = 100 * growth_multiplier ** 7

print(result)




# Other variable types
desc = "compound interest"
profitable = True




# Operations with other types
savings = 100
growth_multiplier = 1.1
desc = "compound interest"

# Assign product of growth_multiplier and savings to year1
year1 = savings * growth_multiplier

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)




# Type conversion
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
float(pi_string)
pi_float = float(pi_string)
