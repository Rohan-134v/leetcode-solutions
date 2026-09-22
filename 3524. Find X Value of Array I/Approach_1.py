class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
    
        for num in nums:
            new_dp = [0] * k
            val = num % k
        
            new_dp[val] += 1
        
            for rem in range(k):
                if dp[rem] > 0:
                    new_dp[(rem * val) % k] += dp[rem]
                
            for i in range(k):
                ans[i] += new_dp[i]
            
            dp = new_dp
        
        return ans