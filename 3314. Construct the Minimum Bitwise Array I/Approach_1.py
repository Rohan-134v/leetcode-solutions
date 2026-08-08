class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                b = 1
                while (num & b) != 0:
                    b <<= 1
                
                ans.append(num-(b >> 1))
        return ans
