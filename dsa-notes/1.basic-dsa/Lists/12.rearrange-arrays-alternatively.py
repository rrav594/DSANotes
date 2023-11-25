class Solution:
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        max_ = arr[n-1]+1
        min_index, max_index = 0, n-1
        for i in range(n):
            if i%2 == 0:
                arr[i] += (arr[max_index]%max_) * max_
                max_index -= 1
            else:
                arr[i] += (arr[min_index]%max_) * max_
                min_index += 1
        for i in range(n):
            arr[i] = arr[i] // max_
        return arr

