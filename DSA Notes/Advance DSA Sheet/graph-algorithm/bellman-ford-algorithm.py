class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dis = [float("inf") for i in range(V)]
        dis[S] = 0
        for _ in range(V-1):
            for u, v, w in edges:
                dis[v] = min(dis[v], dis[u]+w)
        for u, v, w in edges:
            if dis[u] != float("inf") and dis[u] + w < dis[v]:
                return [-1]
        for i in range(V):
            if dis[i] == float("inf"):
                dis[i] = 10**8
        return dis