class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            dp[idx] = (1 + sum(dp)) % MOD
            
        return sum(dp) % MOD