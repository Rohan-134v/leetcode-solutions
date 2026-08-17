class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        for i in range(n - 1, -1, -1):
            m = i - 1
            for j in range(i + 1, n):
                while m + 1 < j and (prefix[m + 2] - prefix[i]) * 2 <= prefix[j + 1] - prefix[i]:
                    m += 1
                    
                res = 0
                if m >= i:
                    left_sum = prefix[m + 1] - prefix[i]
                    total_sum = prefix[j + 1] - prefix[i]
                    if left_sum * 2 == total_sum:
                        res = max(res, max_l[i][m])
                        res = max(res, max_r[m + 1][j])
                    else:
                        res = max(res, max_l[i][m])
                        if m + 1 < j:
                            res = max(res, max_r[m + 2][j])
                else:
                    res = max(res, max_r[i + 1][j])
                    
                dp[i][j] = res
                current_sum = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], res + current_sum)
                max_r[i][j] = max(max_r[i + 1][j], res + current_sum)
                
        return dp[0][n - 1]