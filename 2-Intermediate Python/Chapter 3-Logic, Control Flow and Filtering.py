# DataCamp Data Scientist with Python
# 2-Intermediate Python
# Chapter 3-Logic, Control Flow and Filtering

# Equality
# Comparison of booleans
print(True == False)

# Comparison of integers
print((-5 * 15) != 75)

# Comparison of strings
print("pyscript" == "PyScript")

# Compare a boolean with an integer
print(True == 1)




# Greater and less than
# Comparison of integers
x = -3 * 6
print(x>=-10)


# Comparison of strings
y = "test"
print("test"<=y)


# Comparison of booleans
True > False




# Compare arrays
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)




# and, or, not (1)
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen < 10 and my_kitchen > 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen > 14 or my_kitchen < 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)




# Boolean operators with NumPy
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))




# if
# Define variables
room = "kit"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen.")

if area > 15 :
    print("big place!")




# Add else
# Define variables
room = "kit"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

if area > 15 :
    print("big place!")
else :
    print("pretty small.")




# Customize further: elif
# Define variables
room = "bed"
area = 14.0

if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

if area > 15 :
    print("big place!")
elif area > 10 :
    print("medium size, nice!")
else :
    print("pretty small.")





# Driving right (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

dr = cars["drives_right"]
sel = cars[dr]

"drives_right" == True
print(sel)





# Driving right (2)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

sel = cars[cars['drives_right']]
print(sel)




# Cars per capita (1)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

cpc = cars["cars_per_cap"]

many_cars = cpc > 500

car_maniac = cars[many_cars]
print(car_maniac)





# Cars per capita (2)
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

import numpy as np
cpc = cars['cars_per_cap']


medium = cars[np.logical_and(cpc > 100, cpc < 500)]

print(medium)

