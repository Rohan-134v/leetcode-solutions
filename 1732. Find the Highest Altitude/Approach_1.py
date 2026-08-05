class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = 0
        altitude = 0
        for i in range(len(gain)):
            altitude += gain[i]
            maximum = max(maximum, altitude)

        return maximum