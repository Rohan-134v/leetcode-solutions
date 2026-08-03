# 1456. Maximum Number of Vowels in a Substring of Given Length

### Difficulty: Medium

## Description
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
Example 1:


Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.


Example 2:


Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.


Example 3:


Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	1 <= k <= s.length

## Submission Details
- **Status**: Accepted
- **Runtime**: 43
- **Memory**: 19632000
- **Language**: python3

## Code
```python3
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
```
