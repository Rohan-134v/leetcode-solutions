# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

### Difficulty: Hard

## Description
You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 
Example 1:


Input: s = "baba", target = "abba"

Output: "baab"

Explanation:


	The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
	The lexicographically smallest permutation that is strictly greater than target is "baab".



Example 2:


Input: s = "baba", target = "bbaa"

Output: ""

Explanation:


	The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
	None of them is lexicographically strictly greater than target. Therefore, the answer is "".



Example 3:


Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".


Example 4:


Input: s = "aac", target = "abb"

Output: "aca"

Explanation:


	The only palindromic permutation of s is "aca".
	"aca" is strictly greater than target. Therefore, the answer is "aca".



 
Constraints:


	1 <= n == s.length == target.length <= 300
	s and target consist of only lowercase English letters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 14
- **Memory**: 19360000
- **Language**: python3

## Code
```python3
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
```
