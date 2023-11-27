
class Solution:
    #Heapify function to maintain heap property.
    def parent(self, i):
        return (i-1)//2
    def lchild(self, i):
        return 2*i+1
    def rchild(self, i):
        return 2*i+2
    def heapify(self,arr, n, i):
        left = self.lchild(i)
        right = self.rchild(i)
        largest = i
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(self.parent(n-1), -1, -1):
            self.heapify(arr, n, i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        # Min Heap is build
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr