
import singleRouterGlobalConstants as gc
import networkEquations as ne

class SingleRouterNetworkState:
    def __init__(self, dropAlgArg='red'):
        self.flows = [] # routers
        self.q_history = [175]
        self.p_history = [0]
        self.rtt_hist = [3]
        self.x_hist = [0]
        self.C = gc.CMAX # max queue capacity
        self.dropAlg = dropAlgArg
        self.t_max = gc.TMAX
        self.t_min = gc.TMIN
        self.p_max = gc.PMAX
        self.alpha = gc.ALPHA
        self.sigma = gc.SIGMA
        self.x = 0 # average predicted queue length
    
    def addFlow(self, flow):
        # add router to list
        # calculation rtt
        self.flows.append(flow)

    def getProbDrop(self, t):
        if t < 0:
            t = 0
        else:
            t = round(t)
        if self.dropAlg == 'red':
            return ne.redDropProb(self.t_min, self.t_max, self.x_hist[t], self.p_max)
        elif dropAlg == "dropTail":
            return ne.dropTailDropProb(self.t_max)
        else:
            raise Exception("dropAlg not recognized")


    def getRtt(self, flowNum, t):
        if (t<0):
            t = 0
        t = round(t)
        # print("Flow num, t, q_hist_len, flowLen = ", flowNum, t, len(self.q_history), len(self.flows))
        return ne.rtt(self.q_history[t], self.C, self.flows[flowNum].T_prop)

    def getCurQ(self):
        return self.q_history[-1]

    def evolve(self, t):
        
        step = 0.01
        print(t)
        print("qhist: ", self.q_history[t-1])
        
        qDelta = step * ne.q_dt(self, t)
        for i in range(len(self.flows)):
            wDelta = step * ne.w_i_dt(self, t, i)
            newW = self.flows[i].getW(t) + wDelta
            if newW < 0:
                newW = 0
            self.flows[i].W.append(newW)
        # except:
            # print(self.q_history)
            # self.flows[i].rtt.append(ne.rtt(self.q_history[t], self.C, self.flows[flowNum].T_prop))

        
        newQ = self.q_history[t] + qDelta
        print("q_hist, delta q, Q:", self.q_history[t], qDelta, newQ)

        if (newQ < 0):
            self.q_history.append(0)
            # print("newQ < 0")
        else:
            self.q_history.append(newQ)
            # print("newQ > 0")

        xDelta = step * ne.x_dt(self, self.alpha, self.sigma)
        self.x += xDelta
        if self.x < 0:
            self.x = 0
        self.x_hist.append(self.x)
        print("q_hist, w, x: ", self.q_history[t], wDelta, xDelta)


        # calculatio q_dt
        # for each flow:
            # calculate W_i_t
            # update W_i
            # append W_i

        # update q
        # append q
        # update x


class Flow:
    def __init__(self, initT_prop=gc.TPROP, initW=100):
        self.W = [initW]
        self.rtt = [initT_prop]
        self.T_prop = initT_prop

    def getW(self, t):
        if t < 0:
            t = 0
        else:
            t = round(t)
        return self.W[t]

    def getRtt(self, t):
        if t < 0:
            t = 0
        else:
            t = round(t)
        return self.rtt[t]

    

