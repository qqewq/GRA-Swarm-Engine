import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)+1e-8)

def resonance_matrix(states):

    n=len(states)
    R=np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            R[i,j]=cosine_similarity(states[i],states[j])

    return R