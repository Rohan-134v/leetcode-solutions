class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        q1, q2 = 0, 0
        s1, s2 = 0, 0

        for i in range(n):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])

        for i in range(n,len(num)):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])

        if (q1 + q2) % 2 != 0:
            return True
        
        if (s1 - s2) * 2 == 9 * (q2 - q1):
            return False

        return True
        
