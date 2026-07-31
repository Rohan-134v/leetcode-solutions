class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        opr = 0
        while left < right :
            sum_2 = nums[left] + nums[right]
            if sum_2 == k:
                opr += 1
                left += 1
                right -= 1
            elif sum_2 < k:
                left += 1
            else:
                right -= 1
            
        return opr