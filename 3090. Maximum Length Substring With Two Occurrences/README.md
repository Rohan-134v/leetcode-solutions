# 3090. Maximum Length Substring With Two Occurrences

### Difficulty: Easy

## Description
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 
Example 1:


Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:


Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

 
Constraints:


	2 <= s.length <= 100
	s consists only of lowercase English letters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 3
- **Memory**: 19172000
- **Language**: python3

## Code
```python3
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        hashmap = {}
        ans = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            while hashmap[s[right]] > 2:
                hashmap[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans
```
