import multi_arm_bandits.bandits as bandit
import learning_algorithm.epsilon_greedy as egreedy


def main():
    print("Hello world")
    b1 = bandit.Bandit(10)
    agent = egreedy.epsilonAgent()
    agent.Run(10000, b1)
    print("printing best arm")
    print(b1.getBestArm())
    print("printing best estimate")
    print(agent.getBestEstimate())
main()