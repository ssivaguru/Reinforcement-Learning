import multi_arm_bandits.bandits as bandit
import learning_algorithm.epsilon_greedy as egreedy


def main():
    print("Hello world")
    b1 = bandit.Bandit(10)
    b1.createDistribution(3)
    egreedy.Print()

main()