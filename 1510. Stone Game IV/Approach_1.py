class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n < 1:
            return False
        dp = [False] * (n+1)
        for i in range(1,n+1):
            for k in range(1, math.isqrt(i) + 1):
                if not dp[i-k*k]:
                    dp[i] = True
                    break
        return dp[n]
