
import numpy as np
import math as m



# differential equations

def w_i_dt(netState, t, flowNum):

    R_i_t = netState.getRtt(flowNum, t)

    R_i_former = netState.getRtt(flowNum, t-R_i_t)
    W_i_t = netState.flows[flowNum].getW(t)
    W_i_former = netState.flows[flowNum].getW( t- R_i_t)
    dropProb_former = netState.getProbDrop(t-R_i_t)

    return 1 / R_i_t - dropProb_former * (W_i_t * W_i_former) / (2 * R_i_former) 

def q_dt(netState, t):
    ratioSum = 0
    for flowNum in range(len(netState.flows)):
        f = netState.flows[flowNum]
        ratioSum += f.getW(t) / netState.getRtt(flowNum, t)
    
    return -netState.C + ratioSum

def x_dt(netState, alpha, sigma):
    # print(m.log(1-alpha)/sigma)
    # return m.log(1-alpha)/sigma * netState.x - m.log(1-alpha)/sigma * netState.getCurQ()
    K = -m.log(1-alpha)/sigma
    print(K)
    # K = 1.0000500033334732
    return - K  * netState.x + K * netState.getCurQ()

# helper equations
def rtt(q, C, T_prop):
    # q is the queue length
    # C is the max queue capacity
    # T_prop is the propagation time
    return T_prop + q / C

def redDropProb(t_min, t_max, x, p_max):
    # t_min = min queue length for dropping
    # t_max = max allowable queue length
    # x = queue length prediction

    if (x < 0):
        raise Exception("predicted queue length < 0")
    if x < t_min:
        return 0
    elif x > t_max:
        return 1
    else:
        return (x - t_min)/(t_max - t_min) * p_max

def dropTailDropProb(t_max, q):
    # q = queue length
    # t_max = max allowable queue length
    if (q < t_max):
        return 0
    else:
        return 1