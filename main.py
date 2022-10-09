import multi_arm_bandits.bandits as bandit
import learning_algorithm.ucb as upperConfidanceBound


def main():
    print("Hello world")
    b1 = bandit.Bandit(10)
    agent = upperConfidanceBound.ucb(b1.getNoArms())
    agent.run(1000, b1)
    print(b1.getBestArm())
    print(agent.getBestEstimate())
main()