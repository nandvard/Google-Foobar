#import numpy as np

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x%y)


def willLoop(a,b):

    # Brute Force - too slow
    # Play the game and keep track of count of bananas with each guard
    # If both counts are same, game over. If either count was seen earlier, it's an infinite loop
##    seen = {}
##
##    while(a != b):
##        if a < b:
##            b = b-a
##            a = a+a
##        elif a > b:
##            a = a-b
##            b = b+b
##             
##        if a in seen:   # or b in seen:
##            return True
##        else:
##            seen[a] = seen[b] = True
##        
##    return False

    # Found this method on internet
    n = (a+b) / gcd(a,b)

    if n == int(n):                 # If value is integer
        n = int(n)                  # Convert float datatype to int
        return (n & (n-1)) != 0     # If n is not a power of 2, they will loop
    else:
        return True


def checkAllPairs(List):
    graph = [[0]*len(List) for i in range(len(List))]               # Graph Adjacency Matrix
    
    for i in range(len(List)-1):
        for j in range(i+1,len(List)):
            graph[i][j] = graph[j][i] = willLoop(List[i],List[j])   #Add edge between two nodes if they loop

    return graph


def getMaxMatchingPairs(graph):
    """
    Greedy Algorithm
    Sort nodes by number of edges
    Pair the smallest node with its next pair-able node
    Disconnect both nodes from graph
    Repeat until all nodes are disconnected
    """

    match = []

    while sum(map(sum,graph)) > 0:  # While graph has atleast 1 edge remaining, sum of edges in adjacency matrix is not zero

        edge_count = [[i,sum(e)] for i,e in enumerate(graph)]   # Count number of edges of each node
        edge_count.sort(key = lambda x: x[1])                   # Sort nodes by number of edges
        
        foundMatch = 0
        # Loop through each pair of nodes
        for i in range(len(edge_count)-1):
            for j in range(i+1,len(edge_count)):
                if foundMatch == 0:
                    node1 = edge_count[i][0]
                    node2 = edge_count[j][0]

                    if graph[node1][node2] == 1:                    # If the nodes match (which will also ignore disconnected nodes since they have no edges)
                        match.append([node1,node2])                 # Pair them
                        foundMatch = 1                              # Flag to 'break' out of double for loop i.e. ignore other pairs of nodes, until graph is re-sorted
                        for i in range(len(graph)):                  
                            graph[i][node1] = graph[node1][i] = 0   # Disconnect both nodes from graph,
                            graph[i][node2] = graph[node2][i] = 0   # by removing all their edges

    return match


def solution(banana_list):
    #print ('banana_list=',banana_list)

    graph = checkAllPairs(banana_list)
    #print ('graph=\n',np.matrix(graph))
    
    match = getMaxMatchingPairs(graph)
    #print('match=', [[banana_list[m[0]],banana_list[m[1]]] for m in match] )

    return (len(banana_list) - 2*len(match))
    

print (solution( [2,6,10,30,22,42] ))
