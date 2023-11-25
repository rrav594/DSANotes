import heapq
from collections import Counter
class Solution :
    def rearrangeString(self, str):
        #code here
        d = Counter(str)
        maxFreq = 0
        for k in d:
            if d[k] > maxFreq:
                maxFreq = d[k]
        if maxFreq > (len(str)+1)//2:
            return "0"
        heap = []
        for k in d:
            heapq.heappush(heap, [-d[k], k])
        prev = [1, "$"]
        str = ""
        while heap:
            count, char = heapq.heappop(heap)
            count += 1
            str += char
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = [count, char]
        return str