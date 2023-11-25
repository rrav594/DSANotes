class Solution:
	def isNegativeWeightCycle(self, n, edges):
	    if n == 0 or n == 1:
	        return 0
		dis = [float("inf") for i in range(n)]
		dis[edges[0][0]] = 0
		for i in range(n-1):
		    for u, v, w in edges:
		        if dis[u] != float("inf") and dis[v] > dis[u]+w:
		            dis[v] = dis[u]+w
	    for u, v, w in edges:
	        if dis[u] != float("inf") and dis[u]+w < dis[v]:
	            return 1
	    return 0