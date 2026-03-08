# GRA Swarm Architecture

## System

Agents explore a solution space:

s_i ∈ S

Each state is evaluated by resonance with others.

## Resonance

R(i,j) = similarity(s_i , s_j)

Example:

cosine similarity

Total amplification:

A_i = Σ R(i,j)

Agents with higher resonance survive and mutate.

## Evolution

selection → mutation → new swarm

## Emergence

With many agents:

- clusters appear
- swarm converges
- collective search improves