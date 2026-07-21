class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

        return nums[len(nums) -1]