##implementation of epsilon greedy algorithm

import numpy as np
from random import randrange
from multi_arm_bandits import bandits
import time 
from learning_algorithm.action_value import ActionValue 


class epsilonAgent():
    def __init__(self):
        self.actionValue = ActionValue()
        
    def __choose_random(self):
        return np.random.randn()
    
    def __choose_best_arm(self):
        return np.argmax(self.estimate)

    def __choose_arm(self, epsilon, bandit, epoch):

        p = self.__choose_random()
        arm  = 0
        if p < epsilon:
            arm = randrange(bandit.getNoArms())
        else:
            arm = self.actionValue.getBestArm()
        reward = bandit.pullArm(arm)
        stepsize = 1 / ( (epoch/ 50) + 1 )
        self.actionValue.updateEstimate(arm , reward, stepsize)


    def __step_reduce_epsilon(self, epsilon):
        if epsilon <= 0.3:
            return epsilon
        return epsilon - 0.1
    
    def Run(self, epoch, bandit):
        if epoch < 100:
            print("Minimum expected epoche is 100")
            return
        
        epsilon = 0.9
        
        arms = bandit.getNoArms()
        self.actionValue.createRewardEstimates(arms)
        count = 1
        while count != epoch:
            self.__choose_arm(epsilon, bandit, count)
            count+=1
            if count % 300 == 0:
                epsilon = self.__step_reduce_epsilon(epsilon)
    
    def getBestEstimate(self):
        return self.actionValue.getBestArm()
    

