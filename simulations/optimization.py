import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agents.agent import Agent
from swarm.swarm import Swarm

agents=[Agent() for _ in range(50)]

swarm=Swarm(agents)

for step in range(200):

    swarm.evaluate()

    best=max(a.score for a in swarm.agents)

    print("step",step,"best resonance",best)

    swarm.select_and_evolve()