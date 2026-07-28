# 3517. Smallest Palindromic Rearrangement I

### Difficulty: Medium

## Description
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 
Example 1:


Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.


Example 2:


Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.


Example 3:


Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	s is guaranteed to be palindromic.

## Submission Details
- **Status**: Accepted
- **Runtime**: 168
- **Memory**: 21032000
- **Language**: python3

## Code
```python3
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        counts = Counter(s)
        first_half = []
        mid_char = ""

        for char in sorted(counts.keys()):
            if counts[char] % 2 != 0:
                mid_char = char

            first_half.append(char * (counts[char] // 2))
        
        first_half_str = "".join(first_half)

        return first_half_str + mid_char + first_half_str[::-1]

```
