class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        beg, ed = 0, 1
        while ed < len(nums):
            while beg < len(nums) and nums[beg]:
                beg += 1
            ed = max(ed, beg)
            while ed < len(nums) and not nums[ed]:
                ed += 1
            if ed == len(nums) or beg == len(nums):
                break
            nums[ed], nums[beg] = nums[beg], nums[ed]