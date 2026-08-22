# 3622. Check Divisibility by Digit Sum and Product

### Difficulty: Easy

## Description
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:


	
	The digit sum of n (the sum of its digits).
	
	
	The digit product of n (the product of its digits).
	


Return true if n is divisible by this sum; otherwise, return false.

 
Example 1:


Input: n = 99

Output: true

Explanation:

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.


Example 2:


Input: n = 23

Output: false

Explanation:

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.


 
Constraints:


	1 <= n <= 106

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 19352000
- **Language**: python3

## Code
```python3
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product, total = 1, 0
        a = n
        while a > 0:
            temp = a % 10
            total += temp
            product *= temp
            a = a // 10
        
        print(total + product)
        
        return True if n % (total + product) == 0 else False
```
