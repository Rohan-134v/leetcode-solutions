# 345. Reverse Vowels of a String

### Difficulty: Easy

## Description
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:


Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


Example 2:


Input: s = "leetcode"

Output: "leotcede"


 
Constraints:


	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 11
- **Memory**: 20392000
- **Language**: python3

## Code
```python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        first = 0
        last = len(s) - 1
        a = list(s)
        owels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U'}
        while first < last :
            if (a[first] in  owels) and (a[last] in owels) :
                a[first], a[last] = a[last], a[first]
                first += 1
                last -= 1
            elif a[first] not in owels:
                first += 1
            elif a[last] not in owels:
                last -= 1
        return "".join(a)


```
