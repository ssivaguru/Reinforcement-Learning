## a common class that implements the Action values methods
## can be used by algorithms that depend on action value
import numpy as np

class ActionValue():

    def __init__(self):
        pass

    def createRewardEstimates(self, no):
        self.estimate = []
        for i in range (no):
            self.estimate.append(0)

    def updateEstimate(self, index, reward, stepsize):
        cur = self.estimate[index]
        cur += cur + stepsize*(reward[0] - cur)
        self.estimate[index] = cur

    def getBestArm(self):
        return np.argmax(self.estimate)
    
    def printestimate(self):
        print(self.estimate)

    
