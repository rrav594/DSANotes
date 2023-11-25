class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        def find(x, parent):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x], parent)
            return parent[x]
        def union(x, y):
            x_rep, y_rep = find(x, parent), find(y, parent)
            if x_rep == y_rep:
                return 
            if rank[x_rep] < rank[y_rep]:
                parent[x_rep] = y_rep
            elif rank[x_rep] > rank[y_rep]:
                parent[y_rep] = x_rep
            else:
                parent[y_rep] = x_rep
                rank[y_rep] += 1
        parent = [i for i in range(V)]
        rank = [0 for i in range(V)]
        edges = []
        for i in range(V):
            for nei, weight in adj[i]:
                edges.append([i, nei, weight])
        edges.sort(key=lambda x:x[2])
        res = 0
        for u, v, w in edges:
            us = find(u, parent)
            vs = find(v, parent)
            if us != vs:
                res += w
                union(us, vs)
        return res