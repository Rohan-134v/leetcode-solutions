class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        maximum = max(candies)
        for i in range(len(candies)):
            if maximum <= candies[i] + extraCandies:
                results.append(bool(1))
            else :
                results.append(bool(0))
        return results