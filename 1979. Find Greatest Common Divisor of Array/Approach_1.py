import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)
        return math.gcd(minimum, maximum)