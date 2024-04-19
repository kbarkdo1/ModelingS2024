# Lorenz equations

# import necessary packages
import numpy as np # for general numerical computations
from scipy.integrate import solve_ivp # to solve ODE IVPs
import matplotlib.pyplot as plt # for plotting
from matplotlib import gridspec # for subplot sizes

# start time
t0 = 0 

# end time
tEnd = 50 

# parameter values . chaotic dynamics
s = 10
r = 28
b = 8/3 

# initial values
X0 = np.array([0,  1, 0])

def lorenzODE(t,X,s,r,b):
    x = X[0]
    y = X[1]
    z = X[2]

    dx = s*(y-x)
    dy = r*x-y-x*z
    dz = x*y-b*z

    dX = np.array([dx,dy,dz]);
    return dX

### NUMERICALLY SOLVE THE ODE ####
sol = solve_ivp(lorenzODE, [t0 , tEnd], X0, args=(s,r,b), atol=1e-8 ,rtol=1e-8 )
t = sol.t # time values
x = sol.y[0,:] 
y = sol.y[1,:] 
z = sol.y[2,:] 

# plot results
ax = plt.figure().add_subplot()
ax.plot(t,x,label='x',lw=2)
ax.plot(t,y,label='y',lw=2)
ax.plot(t,z,label='z',lw=2)
ax.legend(loc="upper left")
ax.set_xlabel('t')
ax.set_title('trajectories')

ax = plt.figure().add_subplot(projection='3d')
ax.plot(x,y,z,'k',lw=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('phase space')

plt.show()