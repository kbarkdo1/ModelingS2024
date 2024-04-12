

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath
import math as math

steps = 50
b=10
l=5

alphaVals = [1]
plt.rcParams['font.size'] = 12 # set font size
values = [1]
for i in range(1,steps+1):
    value = l * values[i-1] * (1 + values[i-1])**(-b)
    values.append(value)

plt.plot(values, '.-')
plt.title('Non-zero stability over time')
plt.xlabel('time')
plt.ylabel('values')

plt.show()
