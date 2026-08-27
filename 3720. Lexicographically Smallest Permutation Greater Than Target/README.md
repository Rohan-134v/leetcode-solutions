# 3720. Lexicographically Smallest Permutation Greater Than Target

### Difficulty: Medium

## Description
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 
Example 1:


Input: s = "abc", target = "bba"

Output: "bca"

Explanation:


	The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
	The lexicographically smallest permutation that is strictly greater than target is "bca".



Example 2:


Input: s = "leet", target = "code"

Output: "eelt"

Explanation:


	The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
	The lexicographically smallest permutation that is strictly greater than target is "eelt".



Example 3:


Input: s = "baba", target = "bbaa"

Output: ""

Explanation:


	The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
	None of them is lexicographically strictly greater than target. Therefore, the answer is "".



 
Constraints:


	1 <= s.length == target.length <= 300
	s and target consist of only lowercase English letters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 21
- **Memory**: 19536000
- **Language**: python3

## Code
```python3
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        
        best_branch_idx = -1
        best_branch_char = None
        
        n, m = len(s), len(target)
        
        for i in range(min(n, m) + 1):
            if i == m:
                if n > m: 
                    best_branch_idx = i
                    best_branch_char = None
                break
            
            t_char = target[i]
            
            branch_char = None
            for char in sorted(count.keys()):
                if char > t_char and count[char] > 0:
                    branch_char = char
                    break
            
            if branch_char:
                best_branch_idx = i
                best_branch_char = branch_char
            
            if count[t_char] > 0:
                count[t_char] -= 1
            else:
                break
                
        if best_branch_idx == -1:
            return ""  
            
        result = []
        for i in range(best_branch_idx):
            result.append(target[i])
        rem_count = Counter(s)
        for i in range(best_branch_idx):
            rem_count[target[i]] -= 1
        if best_branch_char is not None:
            result.append(best_branch_char)
            rem_count[best_branch_char] -= 1

        for char in sorted(rem_count.keys()):
            result.extend([char] * rem_count[char])
            
        return "".join(result)
```
