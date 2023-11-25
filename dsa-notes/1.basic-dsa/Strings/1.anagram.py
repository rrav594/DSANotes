from collections import Counter
class Solution:
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
        d = Counter(a)
        for i in range(len(b)):
            if b[i] in d and d[b[i]] > 0:
                d[b[i]] -= 1
            else:
                return False
        return True