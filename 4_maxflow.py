# Bread First Search - Find path from source to destination using Queue
def BFS(graph, src, dest, parent):
    Q = [] 
    visited = [False]*(len(graph))

    Q.append(src)                                   # Add source to Q
    visited[src] = True                             # Set it as visited
    
    while Q:
        u = Q.pop(0)                                # Get first node

        for v in range(len(graph)):                 # Look at all adjacent nodes
            if not visited[v] and graph[u][v] > 0:      # If node not visited (avoids cycle loops and finds shortest route to dest), and edge (with capacity) exists between u-v
                visited[v] = True                           # Set node as visited
                parent[v] = u                               # Set parent node for back tracking
                if v == dest:                               # If path found from src to dest
                    return True                                 # Return Success
                else:                                       # Else
                    Q.append(v)                                 # Add node to Q
                
    return False    # No path found from src to dest, return Failure
          
      
# Graph Maximum Flow - Ford Fulkerson Edmonds Karp algorithm
def maxFlowFFEK(graph, source, sink): 
    
    parent = [-1]*(len(graph))              # To store path from source to destination

    max_flow = 0

    # While any path exists from source to sink
    while BFS(graph, source, sink, parent):

        # Find maximum possible flow (i.e minimum capacity edge) along the path found by BFS
        path_flow = float("Inf")
        v = sink                                            # Start from sink,
        while(v !=  source):
            u = parent[v]                                   # and back track
            path_flow = min(path_flow, graph[u][v])         # Minimum capacity edge
            v = u

        max_flow +=  path_flow              # Add current path flow to overall flow 

        # Update edges with residual flow capacity and add edges with reverse flow
        v = sink
        while(v !=  source): 
            u = parent[v] 
            graph[u][v] -= path_flow        # Residual
            graph[v][u] += path_flow        # Reverse
            v = u 

    return max_flow 


def solution(entrances, exits, path):
    max_bunnies = 0

    # Run max flow method for each set of entrance and exit nodes
    for source in entrances:
        for sink in exits:
            max_bunnies += maxFlowFFEK(path, source, sink)

    return max_bunnies

#print (solution( [0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] ))
