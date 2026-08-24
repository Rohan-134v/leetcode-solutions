class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        p = [0] * n

        p[0] = stones[0]
        for i in range(1,n):
            p[i] = p[i-1] + stones[i]
        
        dp = p[n-1]

        for i in range(n-2,0,-1):
            dp = max(dp,p[i]-dp)
        
        return dp