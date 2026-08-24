class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        read = 0
        write = len(nums) - 1
        
        while read < write:
            if nums[read] % 2 != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write -= 1
            else:
                read += 1
        return nums