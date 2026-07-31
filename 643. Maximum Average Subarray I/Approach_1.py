class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        max_sum = current

        for i in range(k, len(nums)):
            current += nums[i] - nums[i - k]
            if current > max_sum:
                max_sum = current
        return max_sum/k