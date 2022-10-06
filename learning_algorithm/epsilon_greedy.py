
import numpy as np
from random import randrange
from multi_arm_bandits import bandits

class epsilonAgent():
    def __init__(self) -> None:
        self.stepsize = 0.5
        pass
    
    def __choose_random(self):
        return np.random.randn()

    def __create_reward_estimate(self, arms):
        self.estimate = []
        for i in range (arms):
            self.estimate.append(0)
    
    def __update_estimate(self, arm, reward):
        cur = self.estimate[arm]


        cur += cur + self.stepsize*(reward[0] - cur)
        self.estimate[arm] = cur
    
    def __choose_best_arm(self):
        return np.argmax(self.estimate)

    def __choose_arm(self, epsilon, bandit):

        p = self.__choose_random()
        arm  = 0
        if p < epsilon:
            arm = randrange(bandit.getNoArms())
        else:
            arm = self.__choose_best_arm()

        print(arm)
        reward = bandit.pullArm(arm)
        self.__update_estimate(arm , reward)

    def __step_reduce_epsilon(self, epsilon):
        return epsilon - 1
    
    def Run(self, epoch, bandit):
        if epoch < 100:
            print("Minimum expected epoche is 100")
            return
        
        epsilon = 1
        
        arms = bandit.getNoArms()
        self.__create_reward_estimate(arms)
        while epoch != 0:
            self.__choose_arm(epsilon, bandit)
            epoch = epoch - 1
            if epoch % 200 == 0:
                epsilon = self.__step_reduce_epsilon(epsilon)
    
    def printestimate(self):
        print("computed is")
        print(self.estimate)

