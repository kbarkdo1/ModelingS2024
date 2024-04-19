

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath
import math as math

steps = 1000
# k = 0.5

# kVals = [0.25, 0.5, 2, 4, 10]
# for proportions:
kVals = [3, 5, 7, 9, 11, 13]
# kVals = [2, 4, 6, 8, 10]
# kVals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kVals = [1.75, 2.75, 3.75, 4.75, 5.75, 6.75, 7.75, 8.75, 9.75, 10.75]
# kVals = [2, 2.5, 2.75, 3, 3.33, 3.5, 4]
plt.rcParams['font.size'] = 12 # set font size
fig, ax = plt.subplots(len(kVals))
fig.suptitle("k Variance")
plt.subplots_adjust(bottom=0.1,top=0.9, left=.05, right=0.95)
counts = [0]*len(kVals)

for kIn in range(len(kVals)):
    values = [math.sqrt(2)-1]
    k=kVals[kIn]
    stable = 1/(1+k)
    for i in range(1,steps+1):
        if values[i-1] < 0:
            value = values[i-1]+1
        else:
            value = -k*values[i-1]+1
        if value > stable:
            counts[kIn] += 1
        values.append(value)
        if kIn == 0:
            print(value)
    counts[kIn] = counts[kIn] / len(values)

    ax[kIn].plot(values, '.-')
    ax[kIn].set_title('k='+str(k))
    ax[kIn].set_xlabel('time')
    ax[kIn].set_ylabel('values')

table = np.array([kVals, counts])
print(table.T)
print(counts)
fig.tight_layout(pad=5.0)
plt.show()

