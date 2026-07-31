class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('INF')
        second = float('INF')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False