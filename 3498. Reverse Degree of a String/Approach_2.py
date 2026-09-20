class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for i, ch in enumerate(s):
            degree += (123-ord(ch))*(i+1)
        return degree