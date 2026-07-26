class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)
        op1 = nums[0] * nums[1] * nums[a - 1]
        op2 = nums[a - 1] * nums[a - 2] * nums[a - 3]
        return max(op1, op2)