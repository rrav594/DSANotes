https://www.codingninjas.com/studio/problems/merge-sort_5846?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

def mergeSort(arr: [int], l: int, r: int):
    def merge(arr, l, m, h):
        left, right = l, m+1
        res = []
        while left <= m and right <= h:
            if arr[left] <= arr[right]:
                res.append(arr[left])
                left += 1
            else:
                res.append(arr[right])
                right += 1
        while left <= m:
            res.append(arr[left])
            left += 1
        while right <= h:
            res.append(arr[right])
            right += 1
        for i in range(l, h+1):
            arr[i] = res[i-l]
        return arr
    if l >= r:
        return arr
    mid = (l+r)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)
    return arr
