class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximum = 0
        n = len(nums)
        minimum = [0] * (n+1)
        minimum[-1] = nums[-1]
        for i in range(n-1,-1,-1):
            minimum[i] = min(nums[i], minimum[i+1])
        for i in range(n):
            if maximum < nums[i]:
                maximum = nums[i]
            if maximum - minimum[i] <=k:
                return i
        return -1
            
            
