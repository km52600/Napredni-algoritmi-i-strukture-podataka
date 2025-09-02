from collections import deque
from typing import List, Dict, Tuple

def AugmentedHierholzer(G: Dict[str, List[str]], start: str) -> Tuple[List[str], List[List[str]]]:
    """
    Args:
        G (dict): Adjacency matrix implemented as dictionary.
        start (str): Starting node for the algorithm.
    Returns:
        Tuple[List[str], List[List[str]]]: A tuple containing path in Euler graph.
    """
    stack = deque()
    stack.append(start)
    #TODO: 
    visit = []
    C = []
    P = []
    
    while stack:
        u = stack[-1]
        adj = G[u]
        if len(adj) > 0:
            v = G[u][0]
            stack.append(v)
            G[u].remove(v)
            G[v].remove(u)
        else:
            #TODO:
            if len(stack) > 1:
                P.append(stack[-1])
            elif len(stack) == 1:
                P.append(stack[-1])
            visited = stack.pop()
            visit.append(visited)

    for i in range(0,len(visit)-1):
        if visit[i]==visit[i+1]:
            C.append(visit[i])
            break
        else:
            C.append(visit[i])
    #TODO: 
    return (P, C)
