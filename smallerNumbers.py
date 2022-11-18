class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_arr = sorted(nums)
        arr = []
        for num in nums:
            smallers = sort_arr.index(num)
            arr.append(smallers)
        return arr
    