import numpy as np

class Agent:

    def __init__(self, dim=10):
        self.state = np.random.randn(dim)
        self.score = 0

    def mutate(self, sigma=0.1):
        child = Agent(len(self.state))
        child.state = self.state + np.random.randn(len(self.state))*sigma
        return child