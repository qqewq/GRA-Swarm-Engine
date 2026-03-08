"""
Example structure for LLM swarm reasoning.

Replace generate_solution() with real LLM call (OpenAI, local model, etc).
"""

import random

class LLMAgent:

    def __init__(self):
        self.idea=None
        self.score=0

    def generate_solution(self,problem):

        words=["optimize","analyze","decompose","simulate","reason"]
        self.idea=" ".join(random.sample(words,3))

    def mutate(self):

        child=LLMAgent()
        child.idea=self.idea+" improved"
        return child


def score_idea(idea):

    return len(set(idea.split()))


agents=[LLMAgent() for _ in range(10)]

problem="solve optimization problem"

for step in range(20):

    for a in agents:
        a.generate_solution(problem)
        a.score=score_idea(a.idea)

    agents=sorted(agents,key=lambda a:a.score,reverse=True)

    best=agents[0]

    print("step",step,"best idea:",best.idea)

    new_agents=[]

    for a in agents[:5]:
        new_agents.append(a)
        new_agents.append(a.mutate())

    agents=new_agents