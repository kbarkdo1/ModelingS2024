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
tEnd = 100 # units years

t_eval = np.linspace(t0, tEnd, num = 200)

# initial values
S0=.035 
# SN0 = 0.032  # units salinity, PSU
# ST0 = 0.143  # units salinity, PSU
T0 = 260 # starting termparture
x0 = np.array([T0]) # store initial values in a vector

# input function (surface freshwater fluxes, units Sv)
r = 0.01625  # ramping parameter
delH = 0.365 # input strength

tPeak = 1000 

#########  choose one of these inputs #########
#
# ramp function
a = lambda t: 1*(t>tPeak) + (t<=tPeak)*(1./np.cosh(r*(t-tPeak))) 
#
# return function
# a = lambda t: 1/np.cosh(r*(t-tPeak)) 
#########################################

H = lambda t: delH*a(t)  # hosing parameter

def I(t):
    I1 = 0.486+0.1311*H(t) # FN North Atlantic
    I2 = -0.997+0.6961*H(t)  # FT Tropical Atlantic
    I3 = -0.754-0.5646*H(t)  # FIP Indo-Pacific
    I4 = 1.265-0.2626*H(t)  # FS Southern ocean
    return np.array([I1,I2,I3,I4])


# system of ODEs
def AMOCequation(t,x):
    # read in variables from vector x (scaled)
    SN = x[0]  
    ST = x[1] 
    
    # read in input values from input function
    FN  = I(t)[0]*1e6  # [unitsm^3]
    FT  = I(t)[1]*1e6  # [unitsm^3]

    # parameter values [Alkhayoun et al. 2019]
    '''g = 0.36 
    KN = 1.762e6  # [unitsm^3/s]
    KS = 1.872e6  # [unitsm^3/s]
    VN = 0.3683e17 #m^3
    VT = 0.5418e17  #m^3
    VS = 0.6097e17  #m^3
    VIP = 1.4860e17  #m^3
    VB = 9.9250e17  #m^3
    Y = 3.15e7  # sec/year
    C = 4.4735e16  #m^3 (total sum of V*S)'''
    C = 50
    Q = 342
    sigma = 5.67e-8
    e = 0.6

    # model reduction SS, SB, SIP are fixed (slow variables)
    S0 = 0.035  # bacgkground salinity
    SS = (0.034427-S0)*100  # salinity (scaled perturbations from a background state).  
    SB = (0.034538-S0)*100  # salinity (scaled perturbations from a background state).  
    SIP = (100/VIP)*(C-(VN*SN+VT*ST+VS*SS+VB*SB)/100-S0*(VB+VN+VT+VIP+VS))  # Determined from conservation of salinity
 
    # ODE equations [right-hand sides of ODEs]
    q =  Clim(SN,SS) 
    
    # output vector
    dx = np.array([dT]) 
    return dx

def Clim(t, T):
    # 2 x CO2 parameter values for current (not pre-industrial levels)
    C = 50
    Q = 342
    sigma = 5.67e-8
    e = 0.6
    
    q = (1/C) * ((1-(0.5-0.2 *np.tanh((T-265)/10)))*Q - e * sigma * T**4)
    return q



# solve the AMOC equations
# use built-in scipy solver
sol = solve_ivp(Clim, [t0 , tEnd], [260, 264, 265, 270], method='RK45', dense_output=True, t_eval=t_eval)

# values of the variables in the computed solution
t = sol.t
T = sol.y  # North Atlantic salinity flux
# ST = sol.y[1,:]  # Tropical Atlantical salinity flux
# SS = (0.034427-S0)*100  # salinity (scaled perturbations from a background state).  

# AMOC strength. Sv (sverdrup, flux) [1 Sv = 1 million cubic metres per second]
# q = Clim(SN,SS)*1e-6 


# plot results
plt.rcParams['font.size'] = 14 # set font size
fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.1,top=0.95, left=.25, right=0.95)
# plot = plt.plot(t, sol.y[0,:],lw=3)

for tempvect in range(0, sol.y.shape[0]):
    ax.plot(t, sol.y[tempvect,:],lw=3)

ax.set_xlabel('time [years]')
ax.set_ylabel('temperature')
'''
ax[1].plot(t,q,lw=3)
ax[1].set_xlabel('time [years]')
ax[1].set_ylabel('AMOC strength [Sv]')
ax[1].set_ylim([-10, 15])'''

plt.show()


# # plot results
# figure(1)
# subplot(2,1,1), hold all
#     plot(t,H(t),'linewidth',3)
#     ylabel('freshwater hosing [S]')
#     xlabel('time [years]')
#     set(gca,'fontsize',16)
    
# subplot(2,1,2)  hold all
#     plot(t,q,'linewidth',3)
#     ylabel('AMOC strength [Sv]')
#     xlabel('time [years]')
#     set(gca,'fontsize',16)
#     ylim([-10 15])
#     set(gcf,'position',[900 500 900 500])
