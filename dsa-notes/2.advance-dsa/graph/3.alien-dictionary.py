from queue import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
    # count unique characters
        unique = set()
        for word in alien_dict:
            for char in word:
                unique.add(char)
        K = len(unique)
        adj = [[]for i in range(K)]
        for i in range(len(alien_dict)-1):
            word1, word2 = alien_dict[i], alien_dict[i+1]
            start = 0
            while start < len(word1) and start < len(word2):
                if word1[start] != word2[start]:
                    adj[ord(word1[start])-ord('a')].append(ord(word2[start])-ord('a'))
                    break
                start += 1
        color = [0 for i in range(K)]
        return self.topologicalSort(K, adj)
    def topologicalSort(self, V, adj):
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
        for i in range(len(ans)):
            ans[i] = chr(ans[i]+ord('a'))
        return ans
    