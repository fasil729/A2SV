class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        beg, ed, res = 0, 1, 0
        nums.sort()
        while beg < len(nums) - 1:
            ed = max(ed, beg + 1)
            if nums[beg] == nums[beg -1] and beg:
                beg += 1
                continue
            red = nums[ed] - nums[beg]
            if  red < k:
                ed += 1
            elif red == k:
                res += 1
                ed += 1
                beg += 1
            else:
                beg += 1
            if ed == len(nums):
                break
        return res