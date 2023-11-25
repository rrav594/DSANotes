class Solution:
    def MedianOfArrays(self, arr1, arr2):
            #code here
            if len(arr1)>len(arr2):
                arr1,arr2=arr2,arr1
            n1=len(arr1)
            n2=len(arr2)
            target=(n1+n2+1)//2
            s,e=0,n1
            while s<=e:
                mid=(s+e)//2
                mid2=target-mid
                
                l1=float("-inf") if mid==0 else arr1[mid-1]
                h1=float("inf") if mid==n1 else arr1[mid]
                l2=float("-inf") if mid2==0 else arr2[mid2-1]
                h2=float("inf") if mid2==n2 else arr2[mid2]
                
                if l2>h1:
                    s=mid+1
                elif l1>h2:
                    e=mid-1
                else:
                    if (n1+n2)%2==0:
                        res=(min(h1,h2)+max(l1,l2))/2
                        # print(res,int(res),res%1==0)
                        return int(res) if res%1==0 else  res
                    else:
                        return max(l1,l2)
                
            return -1
