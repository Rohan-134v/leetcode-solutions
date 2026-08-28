from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        mid = [c for c, v in freq.items() if v % 2]
        
        if len(mid) > 1:
            return ""
            
        mid_char = mid[0] if mid else ""
        pool = {c: v // 2 for c, v in freq.items()}
        m = len(s) // 2
        
        match_len = 0
        while match_len < m and pool.get(target[match_len], 0) > 0:
            pool[target[match_len]] -= 1
            match_len += 1
            
        for i in range(match_len, -1, -1):
            if i == m:
                res = target[:m] + mid_char + target[:m][::-1]
                if res > target: 
                    return res
            else:
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c > target[i] and pool.get(c, 0) > 0:
                        pool[c] -= 1
                        rem = "".join(ch * pool.get(ch, 0) for ch in "abcdefghijklmnopqrstuvwxyz")
                        half = target[:i] + c + rem
                        return half + mid_char + half[::-1]
            if i > 0:
                pool[target[i-1]] += 1
                
        return ""