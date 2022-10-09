## Implementation of upper confidance bound
from learning_algorithm.action_value import ActionValue 
import numpy as np
from multi_arm_bandits import bandits

class ucb:
    def __init__(self, noArms):
        self.actionValue = ActionValue()
        self.armSelection = []
        self.actionValue.createRewardEstimates(noArms)
        self.confidanceValue = 0.6
        for i in range(noArms):
            self.armSelection.append(1)
        
    def getAction(self, time):
        A_t = []
        estimates = self.actionValue.getEstimates()
        for i in range(len(self.armSelection)):
            A_t.append(estimates[i] + self.confidanceValue * np.sqrt(np.log(time)/ self.armSelection[i]))
        return np.argmax(A_t)

    def run(self, epoch, bandit):
        for i in range(epoch):
            selectedArm = self.getAction(epoch + 1)
            reward = bandit.pullArm(selectedArm)
            self.actionValue.updateEstimate(selectedArm , reward, 1/(i + 1))

    def getBestEstimate(self):
        return self.actionValue.getBestArm()
