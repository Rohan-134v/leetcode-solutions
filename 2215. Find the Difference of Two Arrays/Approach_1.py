class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        results = []
        results.append(list(set([num for num in nums1 if num not in nums2])))
        results.append(list(set([num for num in nums2 if num not in nums1])))
        return results