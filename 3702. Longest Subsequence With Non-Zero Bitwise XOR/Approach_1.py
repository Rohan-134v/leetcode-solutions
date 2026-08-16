class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        if total_xor != 0:
            return len(nums)
            
        if has_nonzero:
            return len(nums) - 1
            
        return 0