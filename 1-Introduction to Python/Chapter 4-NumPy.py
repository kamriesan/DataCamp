# DataCamp Data Scientist with Python
# 1-Introduction to Python
# Chapter 4-Numpy

# Your First NumPy Array
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(np_baseball)

# Print out type of np_baseball
print(type(np_baseball))





# Baseball players' height
# height_in is available as a regular list
print(height_in)

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)


# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)





# Baseball player's BMI
import numpy

np_weight_kg = np.array(weight_lb) * 0.453592
np_height_m = np.array(height_in) * 0.0254
bmi = np_weight_kg / np_height_m ** 2
print(bmi)





# Lightweight baseball players
import numpy as np
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2


light = bmi < 21
print(light)

light = bmi < 21
print(bmi[light])





# Subsetting NumPy Arrays
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

print(np_weight_lb[50])
print(np_height_in[100:111])





# Your First 2D NumPy Array
import numpy
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = numpy.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)




# Baseball data in 2D form
import numpy

np_baseball = np.array(baseball)
print(np_baseball.shape)




# Subsetting 2D NumPy Arrays
import numpy
import numpy

np_baseball = np.array(baseball)
print(np_baseball[49:])

np_weight_lb = (np_baseball[:,1])
print(np_weight_lb)

print(np_baseball[123,0])





# 2D Arithmetic
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

print("start")
# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball+updated)

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)





# Average versus median
# np_baseball is available
import numpy as np
np_height_in = np_baseball[:,0]
print(np.median(np_height_in))
print(np.mean(np_height_in))





# Explore the baseball data

import numpy as np
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))





# Blend it all together

import numpy as np

# converting
np_heights = np.array(heights)
np_positions = np.array(positions)

# extracting
gk_heights = np_heights[np_positions == 'GK']
other_heights = np_heights[np_positions !='GK']


print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))