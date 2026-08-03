class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        maximum_bin = 0
        zeros = 0

        for last in range(len(nums)):
            if nums[last] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start +=  1
            
            maximum_bin = max(maximum_bin, last - start + 1)
        
        return maximum_bin
