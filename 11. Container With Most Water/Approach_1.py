class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        maximum = 0
        while first < last :
            area = min(height[first], height[last]) * (last - first)
            if area >= maximum :
                maximum = area
                if height[first] < height[last]:
                    first += 1
                else:
                    last -= 1
            elif height[first] < height[last]:
                first += 1
            else:
                last -= 1

        return maximum
