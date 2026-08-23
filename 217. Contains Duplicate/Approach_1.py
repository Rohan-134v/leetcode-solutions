class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for num in count.values():
            if num >= 2:
                return True
        
        return False
        
