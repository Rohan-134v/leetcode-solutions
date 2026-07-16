class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(0,len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) -1
                while left < right:
                    total = nums[i] + nums [j] + nums[right] + nums[left]
                    if total == target:
                        results.append([nums[i], nums [j], nums[right], nums[left]])
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    if total > target:
                        right -= 1
                    else:
                        left += 1

        return results