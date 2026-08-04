class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = min(nums)
        return [i for i in range(minimum, maximum+1) if i not in nums ]
