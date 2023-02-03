class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-1 * int(i) for i in nums]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return str(-1 * (heappop(nums)))