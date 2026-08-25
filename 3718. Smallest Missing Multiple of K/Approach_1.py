class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num = set(nums)
        multiple = k

        while multiple in num:
            multiple += k
    
        return multiple
        
        
        