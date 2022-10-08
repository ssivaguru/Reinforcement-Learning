import multi_arm_bandits.bandits as bandit
import learning_algorithm.epsilon_greedy as egreedy


def main():
    print("Hello world")
    b1 = bandit.Bandit(10)
    agent = egreedy.epsilonAgent()
    agent.Run(3000, b1)
    print(b1.getBestArm())
    print(agent.getBestEstimate())
main()