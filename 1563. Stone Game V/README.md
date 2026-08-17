# 1563. Stone Game V

### Difficulty: Hard

## Description
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

 
Example 1:


Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.


Example 2:


Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28


Example 3:


Input: stoneValue = [4]
Output: 0


 
Constraints:


	1 <= stoneValue.length <= 500
	1 <= stoneValue[i] <= 106

## Submission Details
- **Status**: Accepted
- **Runtime**: 670
- **Memory**: 33092000
- **Language**: python3

## Code
```python3
class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        for i in range(n - 1, -1, -1):
            m = i - 1
            for j in range(i + 1, n):
                while m + 1 < j and (prefix[m + 2] - prefix[i]) * 2 <= prefix[j + 1] - prefix[i]:
                    m += 1
                    
                res = 0
                if m >= i:
                    left_sum = prefix[m + 1] - prefix[i]
                    total_sum = prefix[j + 1] - prefix[i]
                    if left_sum * 2 == total_sum:
                        res = max(res, max_l[i][m])
                        res = max(res, max_r[m + 1][j])
                    else:
                        res = max(res, max_l[i][m])
                        if m + 1 < j:
                            res = max(res, max_r[m + 2][j])
                else:
                    res = max(res, max_r[i + 1][j])
                    
                dp[i][j] = res
                current_sum = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], res + current_sum)
                max_r[i][j] = max(max_r[i + 1][j], res + current_sum)
                
        return dp[0][n - 1]
```
