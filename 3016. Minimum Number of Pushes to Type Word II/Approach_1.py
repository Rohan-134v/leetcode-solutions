from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        a = Counter(word)
        freq = sorted(a.values(), reverse = True)
        total = 0
        for idx, cnt in enumerate(freq):
            cost = (idx // 8) + 1
            total += cost*cnt
        return total
            
        
        