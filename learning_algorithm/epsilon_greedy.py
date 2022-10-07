##implementation of epsilon greedy algorithm

import numpy as np
from random import randrange
from multi_arm_bandits import bandits
import time 

class epsilonAgent():
    def __init__(self) -> None:
        pass
    
    def __choose_random(self):
        return np.random.randn()

    def __create_reward_estimate(self, arms):
        self.estimate = []
        for i in range (arms):
            self.estimate.append(0)
    
    def __update_estimate(self, arm, reward, stepsize):
        cur = self.estimate[arm]
        cur += cur + stepsize*(reward[0] - cur)
        self.estimate[arm] = cur
    
    def __choose_best_arm(self):
        return np.argmax(self.estimate)

    def __choose_arm(self, epsilon, bandit, epoch):

        p = self.__choose_random()
        arm  = 0
        if p < epsilon:
            arm = randrange(bandit.getNoArms())
        else:
            arm = self.__choose_best_arm()

        reward = bandit.pullArm(arm)
        self.__update_estimate(arm , reward, 1/epoch)


    def __step_reduce_epsilon(self, epsilon):
        if epsilon <= 0.5:
            return epsilon
        print(epsilon)
        return epsilon - 0.1
    
    def Run(self, epoch, bandit):
        if epoch < 100:
            print("Minimum expected epoche is 100")
            return
        
        epsilon = 0.9
        
        arms = bandit.getNoArms()
        self.__create_reward_estimate(arms)
        count = 1
        while count != epoch:
            self.__choose_arm(epsilon, bandit, count)
            count+=1
            if count % 100 == 0:
                epsilon = self.__step_reduce_epsilon(epsilon)
    
    def printestimate(self):
        print(self.estimate)

