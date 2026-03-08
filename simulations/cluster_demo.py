import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from agents.agent import Agent
from swarm.swarm import Swarm

agents=[Agent(dim=5) for _ in range(100)]
swarm=Swarm(agents)

for step in range(100):

    swarm.evaluate()

    avg=sum(a.score for a in swarm.agents)/len(swarm.agents)

    print("step",step,"avg resonance",avg)

    swarm.select_and_evolve()