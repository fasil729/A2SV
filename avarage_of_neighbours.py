class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1
        j = 2
        while i < len(nums) and j < len(nums):
            nums[i], nums[j] = nums[j], nums[i] 
            i += 2
            j += 2
        return nums