
class epsilonAgent():
    def __init__(self) -> None:
        pass
            
    def Run(epoch, bandit):
        if epoch < 100:
            print("Minimum expected epoche is 100")
            return
        epsilon = 1
        while epoch != 0:

            epoch = epoch - 1

