class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        suffix = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j]:
                suffix[j] = i
                j -= 1

        ans = []
        changed = False
        j = 0

        for i in range(n):
            if j == m:
                break
            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed :
                if j + 1 == m or suffix[j+1] > i:
                    changed = True
                    ans.append(i)
                    j += 1
            
        return ans if len(ans) == m else []





        