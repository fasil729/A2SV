class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = [0 for i in range(len(chalk))]
        prefix_sum[0] = chalk[0]
        for i in range(1,len(chalk)):
            prefix_sum[i] = prefix_sum[i-1] + chalk[i]
        remainder = k % prefix_sum[-1]
        
        #apply binary search on prefix_sum array, target = remainder 
        start = 0
        end = len(prefix_sum) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if remainder == prefix_sum[mid]:
                return mid + 1
            elif remainder < prefix_sum[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start 
