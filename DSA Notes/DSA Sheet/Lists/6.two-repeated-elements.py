class Solution:
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        #Your code here
        res = []
        for i in range(N+2):
            index = abs(arr[i])
            if arr[index] < 0:
                res.append(abs(arr[i]))
            arr[index] = -arr[index]
        return res
    

class Solution:
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        #Your code here
        xor = 0
        x, y = 0, 0
        for i in range(N+2):
            xor ^= arr[i]
        for i in range(1, N+1):
            xor ^= i
        right_set_bit = xor & (-xor)
        for i in range(N+2):
            if arr[i] & right_set_bit:
                x ^= arr[i]
            else:
                y ^= arr[i]
        for i in range(1, N+1):
            if i & right_set_bit:
                x ^= i
            else:
                y ^= i
        return [x, y] 
        