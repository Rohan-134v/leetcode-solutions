# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        last = n

        while start <= last:
            mid = start + (last - start) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                last = mid - 1
            else:
                start = mid + 1
          
        return -1