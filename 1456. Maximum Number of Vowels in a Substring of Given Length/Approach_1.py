class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        owels = set('aeiou')
        count = sum(1 for ch in s[:k] if ch in owels)
        max_owels = count
        for i in range(k,len(s)):
            if s[i] in owels:
                count += 1
            if s[i-k] in owels:
                count -= 1
            max_owels = max(max_owels, count)
            if max_owels == k:
                return k
    
        return max_owels