# 1081. Smallest Subsequence of Distinct Characters

### Difficulty: Medium

## Description
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 
Example 1:


Input: s = "bcabc"
Output: "abc"


Example 2:


Input: s = "cbacdcbc"
Output: "acdb"


 
Constraints:


	1 <= s.length <= 1000
	s consists of lowercase English letters.


 
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19396000
- **Language**: python3

## Code
```python3
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()
    
        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            stack.append(char)
            seen.add(char)
        
        return "".join(stack)
```
