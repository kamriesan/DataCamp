# Introduction to Python Notes Summary

# 1. Python Basics

## ✏️ Hello Python!

### Python as a calculator

- **Exponentiation:** `*`. This operator raises the number to its left to the power of the number to its right. For example `4**2` will give `16`.
- **Modulo:** `%`. This operator returns the remainder of the division of the number to the left by the number on its right. For example `18 % 7` equals `4`.

```python
# Addition, subtraction
print(5 + 5)
print(5 - 5)

# Multiplication, division, modulo, and exponentiation
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)
```

## ✏️ Variables and Types

- Variable
    
    → specific, case-sensitive
    
    → makes codes **reproducible**
    

### Calculate BMI

```python
#Calculate BMI
#height in m, weight in kg

spongebob_height = 1.46
spongebob_weight = 40

bmi = spongebob_weight / (spongebob_height ** 2 )
print(bmi)
```

### Reproducibility

→ changing values

## ✏️ **Other variable types**

- `int` →  integer: a number without a fractional part.
- `float` → floating point: ex. `1.1`
- `str` → represents text. You can use single or double quotes to build a string.
- `bool`  → boolean: a type to represent logical values. Can only be `True` or `False.`

<aside>
💜 **type determiner** can be printed too

```python
icecream_flavor = "vanilla"
print(type(icecream_flavor))
```

</aside>

### Type Conversion

Using the `+` operator to paste together two strings can be very useful in building custom messages.

```python
savings = 100
result = 200
print("I started with $" + float(savings) + " and now have $" + str(result) + ". Awesome!")
```

# 2. Python Lists

## ✏️ Python Lists

- Python lists
    
    → a way to give a single name to a collection of values.
    
    → can be any data type (floats, str, int, boolean, etc.)
    
    → can contain different data types 
    

## ✏️ Subsetting Lists

- Index → used to access information in the list. Starts on 0. `var_name[0]`
    
    ```python
    var_name[0]
    ```
    
    - Example, calling the height of Sprite which is 1.68 `eternals_heights[3]`
    
    ```python
    eternals_heights = ["Thena", 1.73, "Sprite", 1.68, "Gilgamesh", 1.71, "Sersi", 1.89]
    
    **eternals_heights[3]**
    
    # index 0 = "Thena"
    # index 1 = 1.73
    # index 2 = "Sprite"
    # so on and so forth...
    ```
    
    - Using **negative indexes** `var_name[-1]` will call elements at the end of the list
    
    ```python
    eternals_heights = ["Thena", 1.73, "Sprite", 1.68, "Gilgamesh", 1.71, "Sersi", 1.89]
    
    **eternals_heights[-1]**
    
    # index -1 = 1.89
    # index -2 = "Sersi"
    ```
    

### List Slicing

→ Allows to select multiple elements from a list, thus creating a new list. `eternals_heights[3:6]`

```python
eternals_heights = ["Thena", 1.73, "Sprite", 1.68, "Gilgamesh", 1.71, "Sersi", 1.89]

**eternals_Heights[3:6]**
```

→ The result of this will include **index 3-5** only `[1.68, 'Gilgamesh', 1.71]`. The last index `[6]` will not be included.

- List Slicing while leaving out the first or last index.

```python
eternals_heights[:4]
# result will start from index 0 to index 3

eternals_heights[4:]
# result will start from index 4 to the last.
```

### Subsetting Lists of Lists

```python
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
**x[2][:2]**
```

`x[2]` results in a list, that you can subset again by adding additional square brackets.

So inputting `x[2][:2]` will output `**['g', 'h'].**` If we dissect this:

1. `x[2]`→ The third sublist contains `["g", "h", "i"],`
2. `[:2]` → This calls for elements starting from elements `0` to `3` which are `"g and "h".` - *if you’re wondering why `“i”` is not included, it’s because the last element is always ommitted.*

## ✏️ Manipulating Lists

→ change, add, remove elements

### Memory in terms of changing Variables in lists

- Variables do not actually contain all the list values themselves, rather, these contain the **reference** to lists


Example code:

<aside>
💜 I created a custom array for better self-understanding haha

</aside>

```python
# Changing list elements affects Variables
roberts_fam = ["Barbie", "Roberts", "Ken", "Carson"]
roberts_fam_movies = roberts_fam
roberts_fam_movies[0:2] = "Merliah","Summers"
print(roberts_fam)
print(roberts_fam_movies)

# Print Result
# ['Merliah', 'Summers', 'Ken', 'Carson']
# ['Merliah', 'Summers', 'Ken', 'Carson']
```

- When you're updating an element the list, it's one and the same list in the computer memory your changing.
- Both x and y point to this list, so the update is visible from both variables.
- If you want to create a list y that points to a new list in the memory with the same values,

```python
roberts_fam = ["Barbie", "Roberts", "Ken", "Carson"]
roberts_fam_movies = list(roberts_fam)
roberts_fam_movies[0:2] = "Merliah", "Summers"
print(roberts_fam)
print(roberts_fam_movies)

# Print Result
# ['Barbie', 'Roberts', 'Ken', 'Carson']
# ['Merliah', 'Summers', 'Ken', 'Carson']
```

```python
# Replacing one or more element/s in a list
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
x[0:2] = ["w", "x"]
```

---

# 3. Functions and Packages

## ✏️ Functions

### Familiar Function

To get the type of `3.0` and store the output as a new variable

```python
result = type(3.0)
```

The general recipe for calling functions and saving the result to a variable:

```python
output = function_name(input)
```

### Help

To get help on the **`[max()](https://docs.python.org/3/library/functions.html#max)`** function, for example, you can use one of these calls:

```python
help(max)
?max
```

### Multiple Arguments

To tell Python to specify `reverse` without changing anything about `key`, use `=`:

```python
sorted(___, reverse = ___)
```

## ✏️ Methods

| Type | Examples of Methods |
| --- | --- |
| str | capitalize()
 replace() |
| floatl | bit_length()
 conjugate() |
| list | index()
 count() |

### List Methods

```python
# LIST METHODS EXAMPLES
founders_houses = ["helena", "yellow", "rowena", "blue", "godrick", "red", "salazar", "green", "helena", "yellow"]

# 1 index → To show what order in the list is the element 
print(founders_houses.index("godrick"))

# 2 count → To count how many times an element was listed
print(founders_houses.count("helena"))

# 3 append
founders_houses.append("rowena")
```

### String Methods

```python
# STRING METHODS EXAMPLES
founder_house = 'godrick gryffindor'

# 1 capitalize
print(founder_house.capitalize())

# 2 index
print(founder_house.index("c"))

# 3 replace
print(founder_house.replace('godrick gryffindor', 'harry potter'))
```

## ✏️ Packages

→ Directory of python scripts

→ each script = module

### Import Package

`import math`

`import numpy`

### Selective Import

To make import more selective:

```python
from math import pi
from math import radians
```

### **Different ways of importing**

To use the function **`[inv()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.inv.html)`**, which is in the `linalg` subpackage of the `scipy` package:

```python
from scipy.linalg import inv as my_inv
my_inv([[1,2], [3,4]])
```

---

# 4. NumPy

## ✏️ Numpy

Example: When you want to do calculations on lists


```c
import numpy as np
# Numpy Arrays
height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)
print("height")
print(np_height)
print("")

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
print("weight")
print(np_weight)
print("")

bmi = np_weight / np_height ** 2
print("BMI")
print(bmi)
```

Including numpy arrays that have different strings will cause them to print in only one type.

→ numpy is a new Python type, like float string and lists

### Numpy arrays vs python lists

```c
# Numpy Misbehave
python_list = [1, 2, 3]
numpy_Array = np.array([1, 2, 3])
print("Numpy Misbehave")
print(python_list+python_list)
# ^ exact values will be pasted together
print("")

print("Numpy Misbehave")
print(numpy_Array+numpy_Array)
# ^ elements will be added together
print("")
```

### NumPy Array

- Import the `numpy` package as `np`, so that you can refer to `numpy` with `np`.
- Use **`[np.array()](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array)`** to create a `numpy` array from `baseball`. Name this array `np_baseball`.
- Print out the type of `np_baseball` to check that you got it right.

```c
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball) 
print(np_baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

### Baseball players’ height

- Create a `numpy` array from `height_in`. Name this new array `np_height_in`.
- Print `np_height_in`.
- Multiply `np_height_in` with `0.0254` to convert all height measurements from inches to meters. Store the new values in a new array, `np_height_m`.
- Print out `np_height_m` and check if the output makes sense.

```c
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
```

### Baseball players’ BMI

- Create a `numpy` array from the `weight_lb` list with the correct units. Multiply by `0.453592` to go from pounds to kilograms. Store the resulting `numpy` array as `np_weight_kg`.
- Use `np_height_m` and `np_weight_kg` to calculate the BMI of each player. Use the following equation:Save the resulting `numpy` array as `bmi`.
    
    BMI=weight(kg)height(m)2
    
- Print out `bmi`.

```c
import numpy 

np_weight_kg = np.array(weight_lb) * 0.453592
np_height_m = np.array(height_in) * 0.0254
bmi = np_weight_kg / np_height_m ** 2
print(bmi)
```

### Lightweight baseball players

- Create a boolean `numpy` array: the element of the array should be `True` if the corresponding baseball player's BMI is below 21. You can use the `<` operator for this. Name the array `light`.
- Print the array `light`.
- Print out a `numpy` array with the BMIs of all baseball players whose BMI is below 21. Use `light` inside square brackets to do a selection on the `bmi` array.

```python
import numpy as np
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

light = bmi < 21
print(light)

light = bmi < 21
print(bmi[light])
```

### Subsetting NumPy Arrays

```python
# Python List
x = ["a", "b", "c"]
x[1]

# Numpy List
np_x = np.array(x)
np_x[1]
```

## ✏️ 2D Numpy Arrays

### Your First 2D NumPy Array

- Use **`[np.array()](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array)`** to create a 2D `numpy` array from `baseball`. Name it `np_baseball`.
- Print out the type of `np_baseball`.
- Print out the `shape` attribute of `np_baseball`. Use `np_baseball.shape`.

```python
import numpy 
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = numpy.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)
```

### Baseball data in 2D Form

- Use **`[np.array()](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array)`** to create a 2D `numpy` array from `baseball`. Name it `np_baseball`.
- Print out the `shape` attribute of `np_baseball`.

```python
import numpy

np_baseball = np.array(baseball)
print(np_baseball.shape)
```

### Subsetting 2D NumPy Arrays

- Print out the 50th row of `np_baseball`.
- Make a new variable, `np_weight_lb`, containing the entire second column of `np_baseball`.
- Select the height (first column) of the 124th baseball player in `np_baseball` and print it out.

```python
import numpy
import numpy

np_baseball = np.array(baseball)
print(np_baseball[49:])

np_weight_lb = (np_baseball[:,1])
print(np_weight_lb)

print(np_baseball[123,0])
```

### 2D Arithmetic

- You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D `numpy` array, `updated`. Add `np_baseball` and `updated` and print out the result.
- Create a `numpy` array with three values: `0.0254`, `0.453592` and `1`. Name this array `conversion`.
- Multiply `np_baseball` with `conversion` and print out the result.

```python
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
```

## ✏️ Numpy: Basic Statistics (skipped)

### Mean and Median NumPy

`np.mean(x)
 np.median(x)`

### Average versus median

- Create `numpy` array `np_height_in` that is equal to first column of `np_baseball`.
- Print out the mean of `np_height_in`.
- Print out the median of `np_height_in`.

```python
# np_baseball is available
import numpy as np
np_height_in = np_baseball[:,0]
print(np.median(np_height_in))
print(np.mean(np_height_in))
```

### Explore the baseball data

- The code to print out the mean height is already included. Complete the code for the median height. Replace `None` with the correct code.
- Use **`[np.std()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html)`** on the first column of `np_baseball` to calculate `stddev`. Replace `None` with the correct code.
- Do big players tend to be heavier? Use **`[np.corrcoef()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.corrcoef.html)`** to store the correlation between the first and second column of `np_baseball` in `corr`. Replace `None` with the correct code.

```python
import numpy as np
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

### Blend it all together

- Extract all the heights of the goalkeepers. You can use a little trick here: use `np_positions == 'GK'` as an index for `np_heights`. Assign the result to `gk_heights`.
- Extract all the heights of all the other players. This time use `np_positions != 'GK'` as an index for `np_heights`. Assign the result to `other_heights`.
- Print out the median height of the goalkeepers using **`[np.median()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.median.html)`**. Replace `None` with the correct code.
- Do the same for the other players. Print out their median height. Replace `None` with the correct code.

```python
import numpy as np

# converting
np_heights = np.array(heights)
np_positions = np.array(positions)

# extracting
gk_heights = np_heights[np_positions == 'GK']
other_heights = np_heights[np_positions !='GK']

print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))
```
