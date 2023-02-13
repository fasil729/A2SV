class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones, res = 0, 0
        slow, fast = 0, 0
        amm = k

        while fast < len(nums):
            if fast == len(nums) - 1 and amm > 0:
                return len(nums)
            if amm > 0 :
                if nums[fast] == 0:
                    amm -= 1
                fast += 1
            elif amm == 0:
                while fast < len(nums) and nums[fast] == 1:
                    fast += 1
                res = max(res, fast - slow)
                amm -= 1
            else:
                
                if nums[slow] == 0:
                    amm += 1
                    slow += 1
                    fast += 1
                else:
                    slow += 1
                    continue
                
        return res 