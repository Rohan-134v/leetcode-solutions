class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = [m for m in nums1 if m % 2 != 0]
        if min(nums1) % 2 == 0 and len(odd) != 0:
            return False
        else:
            return True