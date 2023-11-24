class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        swaps = 0
        imbalance = 0
        for i in S:
            if i == "[":
                imbalance -= 1
            else:
                imbalance += 1
                if imbalance > 0:
                    swaps += imbalance
        return swaps