class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixsum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefixsum += nums[i]
            else:
                break
        print(prefixsum)
        while prefixsum in nums:
            prefixsum += 1
        
        return prefixsum
