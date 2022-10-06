import multi_arm_bandits.bandits as bandit
import learning_algorithm.epsilon_greedy as egreedy


def main():
    print("Hello world")
    b1 = bandit.Bandit(5)
    agent = egreedy.epsilonAgent()
    agent.Run(1000, b1)
    b1.printestimate()
    agent.printestimate()
main()