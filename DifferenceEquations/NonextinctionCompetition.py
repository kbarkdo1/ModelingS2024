

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath
import math as math

steps = 5000


alphaVals = [1]
colors='rgbm'
startingvales = [
    [0.1, 0.2],
    [0.2, 0.1],
    [2.1, 0.1],
    [0.1, 3/2]
]

plt.rcParams['font.size'] = 12 # set font size
for j in range(len(colors)):
    c = colors[j]
    xvalues = [startingvales[j][0]]
    yvalues = [startingvales[j][1]]

    for i in range(1,steps+1):
        xvalue = (3 * xvalues[i-1]) / (1 + xvalues[i-1] + yvalues[i-1])
        yvalue = (4 * yvalues[i-1]) / (1 + xvalues[i-1] + 2 * yvalues[i-1])
        xvalues.append(xvalue)
        yvalues.append(yvalue)

    plt.plot(xvalues, yvalues, '.-'+c)

plt.title('Non-zero stability over time')
plt.xlabel('x population')
plt.ylabel('y population')

plt.show()
