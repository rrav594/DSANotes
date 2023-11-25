# 1) Using adjacency matrix
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        def graphBuild(V, adj, graph):
            for i in range(V):
                for j in range(len(adj[i])):
                    vertex, weight = adj[i][j]
                    graph[i][vertex] = weight
            return graph
        graph = [[-1 for i in range(V)]for i in range(V)]
        graph = graphBuild(V, adj, graph)
        sptSet = set()
        dis = [float("inf")] * V
        dis[S] = 0
        while len(sptSet) != V:
            min_ = float("inf")
            for u in range(V):
                if u not in sptSet and dis[u] < min_:
                    vertex = u
                    min_ = dis[u]
            sptSet.add(vertex)
            for i in range(V):
                if graph[vertex][i] != -1 and dis[i]>dis[vertex]+graph[vertex][i]:
                    dis[i] = dis[vertex] + graph[vertex][i]
        return dis



# 2) Using adjacency list
import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        def listBuild(V, adj, myList):
            for i in range(V):
                for vertex, weight in adj[i]:
                    myList[i].append([vertex, weight])
            return myList
        myList = [[]for i in range(V)]
        myList = listBuild(V, adj, myList)
        dis = [float("inf") for i in range(V)]
        dis[S] = 0
        heap = []
        heapq.heappush(heap, [S, dis[S]])
        while heap:
            vertex, distance = heapq.heappop(heap)
            for neigh, weight in myList[vertex]:
                if dis[neigh] > dis[vertex]+weight:
                    dis[neigh] = dis[vertex]+weight
                    heapq.heappush(heap, [neigh, dis[neigh]])
        return dis