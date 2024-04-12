

import numpy as np # for general numerical computations
import matplotlib.pyplot as plt # for plotting
import mpmath

steps = 10
f = 4/3
s=1/2

L = np.array([[0, f, f],[s, 0, 0], [0, s, 0]])
x = np.array([1,1,1]).T

gens = 100
for i in range(0, gens):
    x = np.matmul(L, x)

print("After 100 generations:")
print(x)
print("Normalization to 1:")
print(x / x[2])