# 3348. Smallest Divisible Digit Product II

### Difficulty: Hard

## Description
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 
Example 1:


Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.


Example 2:


Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.


Example 3:


Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.


 
Constraints:


	2 <= num.length <= 2 * 105
	num consists only of digits in the range ['0', '9'].
	num does not contain leading zeros.
	1 <= t <= 1014

## Submission Details
- **Status**: Accepted
- **Runtime**: 1684
- **Memory**: 47000000
- **Language**: python3

## Code
```python3
import math
from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                temp_t //= p
        if temp_t > 1:
            return "-1"

        @lru_cache(None)
        def get_shortest(r):
            if r == 1: 
                return ""
            best = None
            for d in range(2, 10):
                nr = r // math.gcd(r, d)
                if nr != r: 
                    cand = get_shortest(nr)
                    if cand is not None:
                        cand = "".join(sorted(str(d) + cand))
                        if best is None:
                            best = cand
                        else:
                            if len(cand) < len(best):
                                best = cand
                            elif len(cand) == len(best) and cand < best:
                                best = cand
            return best
        
        shortest_t = get_shortest(t)
        zero_idx = num.find('0')
        if zero_idx == -1:
            zero_idx = len(num)
        reqs = [t]
        for i in range(min(len(num), zero_idx)):
            reqs.append(reqs[-1] // math.gcd(reqs[-1], int(num[i])))
            
        if zero_idx == len(num) and reqs[-1] == 1:
            return num
            
        for i in range(min(len(num) - 1, zero_idx), -1, -1):
            current_req = reqs[i]
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                nr = current_req // math.gcd(current_req, d)
                short_s = get_shortest(nr)
                
                rem_len = len(num) - 1 - i
                if short_s is not None and len(short_s) <= rem_len:
                    return num[:i] + str(d) + "1" * (rem_len - len(short_s)) + short_s
                    
        req_len = max(len(num) + 1, len(shortest_t))
        return "1" * (req_len - len(shortest_t)) + shortest_t
```
