class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	for i in range(n):
    	    index = arr[i] % n
    	    arr[index] += n
        ans = []
        for i in range(n):
            if arr[i] // n > 1:
                ans.append(i)
        if ans:
            ans.sort()
            return ans
        return [-1]



from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d = Counter(arr)
    	ans = []
    	for i in d:
    	    if d[i] > 1:
    	        ans.append(i)
        if ans:
            ans.sort()
            return ans
        return [-1]