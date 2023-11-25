class Solution:
	def shortest_distance(self, matrix):
		#Code here
		def replace(a, b, mat):
		    for i in range(len(mat)):
		        for j in range(len(mat[0])):
		            if mat[i][j] == a:
		                mat[i][j] = b
		    return mat
	    replace(-1, float("inf"), matrix)
		row, col = len(matrix), len(matrix[0])
	    for k in range(len(matrix)):
    	    for i in range(row):
	            for j in range(col):
	                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
	    replace(float("inf"), -1, matrix)
	    return matrix