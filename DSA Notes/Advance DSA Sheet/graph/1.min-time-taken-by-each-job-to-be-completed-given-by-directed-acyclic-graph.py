# Topological Sorting
from queue import deque
class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        def buildList(edges, adj):
            for i in edges:
                u, v = i
                adj[u].append(v)
            return adj
        adj = [[]for i in range(n+1)]
        adj = buildList(edges, adj)
        indegree = [0 for i in range(n+1)]
        q = deque()
        for i in range(1, n+1):
            for j in adj[i]:
                indegree[j] += 1
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
        timer = 0
        time = [0 for i in range(n+1)]
        while q:
            timer += 1
            size = len(q)
            for i in range(size):
                vertex = q.popleft()
                time[vertex] = timer
                for i in adj[vertex]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return time[1:]
        


