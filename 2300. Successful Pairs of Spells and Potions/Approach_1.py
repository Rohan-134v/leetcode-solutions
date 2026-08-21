class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        n = len(potions)

        for m in spells:
            start = 0
            end = n - 1
            idx = n

            while start <= end:
                mid = (start + end) // 2

                if m * potions[mid] >= success:
                    idx = mid
                    end = mid -1
                else:
                    start = mid + 1
            
            result.append(n - idx)

        return result
                    