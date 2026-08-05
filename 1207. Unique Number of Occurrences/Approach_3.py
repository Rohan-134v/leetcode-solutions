class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for i in range(len(arr)):
            if arr[i] not in h:
                h[arr[i]] = 1
            else :
                h[arr[i]] += 1

        return len(h) == len(set(h.values()))

