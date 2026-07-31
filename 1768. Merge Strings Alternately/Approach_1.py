class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        result = ""
        while a < len(word1) and b < len(word2):
            result = result + word1[a] + word2[b]
            a += 1
            b += 1
        if a < len(word1):
            return result + word1[a:len(word1)]
        else:
            return result + word2[b:len(word2)]
        