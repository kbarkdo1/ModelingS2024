# The AMOC 5-box model of global ocean currenet reduced to two variables
# 
# references Ritchie et al.
#             Rate-induced tipping in natural and human systems
#             Earth Syst. Dynam. 2023
#   
#             Alkhayoun et al.        
#             Basin bifurcations, oscillatory instability and rate-induced thresholds for Atlantic meridional overturning circulation in a global oceanic box model
#             P. Roy. Soc. A-Math. 2019
#

# import necessary packages
import numpy as np # for general numerical computations
from scipy.integrate import solve_ivp # to solve ODE IVPs
import matplotlib.pyplot as plt # for plotting
import mpmath

# start time
t0 =0 

# end time
tEnd = 50 # units

t_eval = np.linspace(t0, tEnd, num = 200)

# initial values
T01=np.array([0,0], dtype="f")
bvec = [0.5, 0.75, 1, 1.25, 1.5]

# system of ODEs
def vanDerPolOscillator(t,v,b):

    # read in variables from vector x (scaled)
    x = v[0]
    y = v[1]

    # output vector
    dT = [(x - 1/3 * x**3 - y), (x-b)]

    dx = np.array(dT) 
    return dx




# plot results
plt.rcParams['font.size'] = 12 # set font size
fig, ax = plt.subplots(len(bvec))
fig.suptitle("b Variance in Van der Pol Equations")
plt.subplots_adjust(bottom=0.1,top=0.9, left=.25, right=0.95)


for i in range(len(bvec)):
    
    b = bvec[i]
    T01[0] = b +0.2
    T01[1] = b- (1/3 * b**3)+0.2
    # solve the equation
    # use built-in scipy solver
    sol = solve_ivp(vanDerPolOscillator, [t0 , tEnd], T01, method='RK45', dense_output=True, t_eval=t_eval, args=(b,))

    # values of the variables in the computed solution
    t = sol.t
    for vect in range(0, sol.y.shape[0]):
        ax[i].plot(t, sol.y[vect,:],lw=3)

    ax[i].set_title('b='+str(b))
    ax[i].set_xlabel('time')
    ax[i].set_ylabel('values')
plt.savefig('bifurcations')
plt.show()

