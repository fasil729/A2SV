class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        heapify(stones)
        while len(stones) >= 2:
            heappush(stones, heappop(stones)-heappop(stones))
        return -1*stones[0]

