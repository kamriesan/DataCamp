# DataCamp Data Scientist with Python
# 2-Intermediate Python
# Chapter 1-Matplotlib

# Line plot (1)
import matplotlib.pyplot as plt
print(year[-1],pop[-1])
plt.plot(year, pop)
plt.show()



# Line plot (3)
import matplotlib.pyplot as plt
print(gdp_cap[-1])
print(life_exp[-1])
plt.plot(gdp_cap, life_exp)
plt.show()



# Scatter Plot (1)
import matplotlib.pyplot as plt
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()



# Scatter plot (2)
import matplotlib.pyplot as plt
plt.scatter(pop, life_exp)
plt.show()



# Build a histogram (1)
import matplotlib.pyplot as plt
plt.hist(life_exp)
plt.show()



# Build a histogram (2): bins
import matplotlib.pyplot as plt
plt.hist(life_exp,5)
plt.show()
plt.clf()

plt.hist(life_exp,20)
plt.show()
plt.clf()


# Build a histogram (3): compare
plt.hist(life_exp,15)

plt.show()
plt.clf()

plt.hist(life_exp1950,15)

plt.show()
plt.clf()



# Labels
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

plt.xlabel(xlab)
plt.ylabel(ylab)

plt.title(title)

plt.show()



# Ticks
plt.scatter(gdp_cap, life_exp)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

plt.xticks(tick_val,tick_lab)

plt.show()



#Sizes
import numpy as np
np_pop = np.array(pop)

np_pop = np_pop * 2

plt.scatter(gdp_cap, life_exp, s = np_pop)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

plt.show()



# Colors
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.show()


# Additional Customizations
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

plt.grid(True)

plt.show()