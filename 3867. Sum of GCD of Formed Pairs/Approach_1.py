class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        
        mxi = nums[0]
        for i in range(n):
            if nums[i] > mxi:
                mxi = nums[i]
            prefixGcd.append(math.gcd(nums[i], mxi))
            
        prefixGcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum