class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wp = 0

        for rp in range(len(nums)):
            if nums[rp] != 0:
                nums[rp], nums[wp] = nums[wp], nums[rp]
                wp += 1
 