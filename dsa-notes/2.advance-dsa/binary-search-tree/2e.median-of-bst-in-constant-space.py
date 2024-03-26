#User function Template for python3

def findMedian(root):
    # code here
    # return the median
    def countNodes(root):
        count = 0
        if root is None:
            return count
        curr = root
        while curr:
            if curr.left is None:
                count += 1
                curr = curr.right
            else:
                prev = curr.left
                while prev.right is not None and prev.right is not curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    count += 1
                    curr = curr.right
        return count
    if root is None:
        return 0
    count = countNodes(root)
    currCount = 0
    curr = root
    while curr:
        if curr.left is None:
            currCount += 1
            # Odd case
            if (count % 2 != 0 and currCount == (count + 1)//2):
                return curr.data
            # Even case
            elif (count % 2 == 0 and currCount == (count//2)+1):
                ans = (prev.data + curr.data)/2
                
                return int(ans) if ans*10 == int(ans)*10 else ans
            prev = curr
            #Move to the right
            curr = curr.right    
        else:
            pre = curr.left
            while pre.right != None and pre.right != curr:
                pre = pre.right
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                prev = pre
                currCount += 1
                if (count % 2 != 0 and currCount == (count + 1)//2):
                    return curr.data
                # Even case
                elif (count % 2 == 0 and currCount == (count//2)+1):
                    ans = (prev.data + curr.data)/2
                    return int(ans) if ans*10 == int(ans)*10 else ans
                prev = curr
                curr = curr.right