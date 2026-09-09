class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        pivot = 1000
        while n >= pivot:
            total  += n - pivot + 1
            pivot *= 1000
        return total