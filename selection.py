class Solution:
    def select(self, arr, i):
        if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr[i]
    def selectionSort(self, arr, n):
        for i in range(n-1):
            selected = self.select(arr, i)
            for j in range(i, 0,-1):
                if arr[j-1] > selected:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break
                