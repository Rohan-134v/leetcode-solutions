class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a,2) + int(b,2)
        answer = bin(result)[2:]
        return answer