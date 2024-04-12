

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath
import math as math

steps = 50
beta = 1

alphaVals = [7, 10, 15, 20]
plt.rcParams['font.size'] = 12 # set font size
fig, ax = plt.subplots(len(alphaVals))
fig.suptitle("alpha Variance")
plt.subplots_adjust(bottom=0.1,top=0.9, left=.25, right=0.95)
for kIn in range(len(alphaVals)):
    values = [1]
    alpha=alphaVals[kIn]
    for i in range(1,steps+1):
        value = alpha * values[i-1] * math.e**(-beta * values[i-1])
        values.append(value)

    ax[kIn].plot(values, '.-')
    ax[kIn].set_title('alpha='+str(alpha))
    ax[kIn].set_xlabel('time')
    ax[kIn].set_ylabel('values')

fig.tight_layout(pad=5.0)
plt.show()

