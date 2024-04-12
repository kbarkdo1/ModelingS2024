

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath

steps = 10



G = 10
# k = 1
b = 1/2

kVals = [0.1, 0.5, 1, 2.5]
plt.rcParams['font.size'] = 12 # set font size
fig, ax = plt.subplots(len(kVals))
fig.suptitle("k Variance")
plt.subplots_adjust(bottom=0.1,top=0.9, left=.25, right=0.95)
for kIn in range(len(kVals)):
    values = [80, 100]
    k=kVals[kIn]
    for i in range(2,steps+1):
        value = (1+k)*b* values[i-1] - k*b*values[i-2]+G
        values.append(value)

    ax[kIn].plot(values)
    ax[kIn].set_title('k='+str(k))
    ax[kIn].set_xlabel('time')
    ax[kIn].set_ylabel('values')
plt.show()

