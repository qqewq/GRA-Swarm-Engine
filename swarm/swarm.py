from gra.resonance import resonance_matrix

class Swarm:

    def __init__(self,agents):
        self.agents=agents

    def evaluate(self):

        states=[a.state for a in self.agents]

        R=resonance_matrix(states)

        scores=R.sum(axis=1)

        for i,a in enumerate(self.agents):
            a.score=scores[i]

    def select_and_evolve(self):

        self.agents=sorted(self.agents,key=lambda a:a.score,reverse=True)

        top=self.agents[:len(self.agents)//2]

        new_agents=[]

        for a in top:

            new_agents.append(a)

            new_agents.append(a.mutate())

        self.agents=new_agents