class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in num_map:
                return [num_map[comp], i]
            
            num_map[nums[i]] = i
        return []