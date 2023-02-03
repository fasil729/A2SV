class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        ans = []
        for lis in points:
            l = len(dist)
            val = [(lis[0]**2 + lis[1]**2)**0.5, lis]
            if l + k < len(points):
                heappush(dist, val)
            else:
                ans.append(heappushpop(dist, val)[1])
        return ans