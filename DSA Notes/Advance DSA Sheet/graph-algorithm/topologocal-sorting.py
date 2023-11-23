# 1) KAHN-ALGORITHM
from queue import deque
class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        ans = []
        indegree = [0]*V
        visited = set()
        q = deque()
        for node in range(V):
            for neig in adj[node]:
                indegree[neig] += 1
        for node in range(V):
            if indegree[node] == 0:
                q.append(node)
        while q:
            node = q.popleft()
            visited.add(node)
            ans.append(node)
            for neig in adj[node]:
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    q.append(neig)
        if len(visited) == V:
            return ans
        return -1