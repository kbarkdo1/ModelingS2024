
import globalConstants.py
import networkEquations.py as ne

class SingleRouterNetworkState:
    def __init__(self, c=CMAX, dropAlgArg='red'):
        flows = []
        q_history = [0]
        rtt = [[]] # routers, then RTT history
        p_history = [0]
        C = c # max queue capacity
        dropAlg = dropAlgArg
        t_max = TMAX
        t_min = TMIN
        p_max = PMAX
        alpha = ALPHA
        sigma = SIGMA
        x = 0 # average predicted queue length
    
    def addRouter(self, router, rtt):
        # add router to list
        # calculation rtt

    def getProbDrop(self, t):
        if dropAlg == 'red':
            return ne.redDropProb(self.t_min, self.t_max, self.x, self.p_max)
        elif dropAlg == "dropTail":
            return ne.dropTailDropProb(self.t_max)
        else:
            raise Exception("dropAlg not recognized")


    def getRtt(self, flowNum, t):
        t = round(t)
        if (t<0):
            t = 0
        return rtt(q_hist[t], self.C, self.flows[flowNum].T_prop)

    def getCurQ(self):
        return q_history[-1]

    def evolve(self):
        # calculatio q_dt
        # for each flow:
            # calculate W_i_t
            # update W_i
            # append W_i

        # update q
        # append q
        # update x



class Flow:
    def __init__(self):
        W = []
        qsize = [] # queue history
        

    def getW(self, t):

    def calcAvgQueueLen(self):

    

