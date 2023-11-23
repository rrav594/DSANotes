class Solution:
    def findPairsWithGivenSum(self, target, head):
        first, second = head, head
        ans = []
        while second.next:
            second = second.next
        while first != second and first.prev != second:
            if first.data + second.data == target:
                ans.append([first.data, second.data])
                first = first.next
                second = second.prev
            elif first.data + second.data < target:
                first = first.next
            else:
                second = second.prev
        return ans
