# 2) BFS Approach
def isPossible(self,N,P,prerequisites):
        #code here
        def buildList(pre, adj):
            for u, v in pre:
                adj[v].append(u)
            return adj
        adj = [[]for i in range(N)]
        buildList(prerequisites, adj)
        indegree = [0 for i in range(N)]
        for i in range(N):
            for node in adj[i]:
                indegree[node] += 1
        q = deque()
        count = 0
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)
        while q:
            count += 1
            vertex = q.popleft()
            for node in adj[vertex]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        if count == N:
            return True
        return False

# 1) Using DFS
class Solution:
    def isCyclic(self, N, adj):
        color = [0] * N
        for node in range(N):
            if color[node] == 0:
                if self.dfs(node, adj, color):
                    return True
        return False
    def dfs(self, V, adj, color):
        color[V] = 2
        for node in adj[V]:
            if color[node] == 2:
                return True
            if color[node] == 0 and self.dfs(node, adj, color):
                return True
        color[V] = 1
        return False
    def isPossible(self,N,P,prerequisites):
        #code here
        def buildList(pre, adj):
            for u, v in pre:
                adj[v].append(u)
            return adj
        adj = [[]for i in range(N)]
        buildList(prerequisites, adj)
        ans = self.isCyclic(N, adj)
        return False if ans else True
    

    