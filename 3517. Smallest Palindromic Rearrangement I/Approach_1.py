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
