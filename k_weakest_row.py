class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_of_soldiers = []
        for row in mat:
            num = 0
            for ele in row:
                if ele == 1:
                    num += 1
                else:
                    break
            num_of_soldiers.append(num)
        heap = num_of_soldiers[::]
        heapify(heap)
        weakest = []
        for i in range(k): 
            indice = num_of_soldiers.index(heappop(heap))
            num_of_soldiers[indice] = len(mat[0]) + 1
            weakest.append(indice)
        return weakest
        