class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}
        n = len(nums)

        for i in range(n-k+1):
            unique_nums = set(nums[i:i+k])
            for num in unique_nums:
                count[num] = count.get(num, 0) + 1
            
        res = -1

        for num, c in count.items():
            if c == 1:
                res = max(res, num)    
        return res