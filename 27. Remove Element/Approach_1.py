class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        write = len(nums) 
        while read < write:
            if nums[read] == val:
                nums[read] = nums[write-1]
                write -= 1
            else:
                read += 1
        return write
