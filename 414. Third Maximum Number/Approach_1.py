class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = list(set(nums))
        
        unique.sort()
        if len(unique) < 3:
            return unique[-1]
        
        return unique[-3]
    
    
    