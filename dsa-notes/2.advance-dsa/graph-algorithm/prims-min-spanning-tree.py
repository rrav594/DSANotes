import heapq
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        heap = []
        res = 0
        heapq.heappush(heap, [0, 0])
        visited = set()
        while heap:
            w, node = heapq.heappop(heap)
            if node not in visited:
                res += w
                visited.add(node)
                for nei, wt in adj[node]:
                    if nei not in visited:
                        heapq.heappush(heap, [wt, nei])
        return res