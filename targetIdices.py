class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[j] > nums[j+1]):
                    nums[j] , nums[j+1] = nums[j+1] ,nums[j]
        temp = []
        for i in range(len(nums)):
            if nums[i] == target:
                temp.append(i)
        return temp
    