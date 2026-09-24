class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i,num in enumerate(nums):
            curr_sum = 0
            while num > 0:
                curr_sum  += num % 10
                num = num // 10
            if curr_sum == i:
                return i
            
        return -1 