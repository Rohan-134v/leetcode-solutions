# 3116. Kth Smallest Amount With Single Denomination Combination

### Difficulty: Hard

## Description
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 
Example 1:


Input: coins = [3,6,9], k = 3

Output:  9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.


Example 2:


Input: coins = [5,2], k = 7

Output: 12 

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.


 
Constraints:


	1 <= coins.length <= 15
	1 <= coins[i] <= 25
	1 <= k <= 2 * 109
	coins contains pairwise distinct integers.

## Submission Details
- **Status**: Accepted
- **Runtime**: 153
- **Memory**: 20916000
- **Language**: python3

## Code
```python3
import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for i in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    current_lcm = math.lcm(current_lcm, coins[j])
                    set_bits += 1
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
        def count_valid_amounts(x: int) -> int:
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (x // lcm_val)
            return count

        left = 1
        right = min(coins) * k
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_valid_amounts(mid) >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return result
```
