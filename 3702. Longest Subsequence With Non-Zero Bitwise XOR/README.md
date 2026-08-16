# 3702. Longest Subsequence With Non-Zero Bitwise XOR

### Difficulty: Medium

## Description
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

 
Example 1:


Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.


Example 2:


Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.


 
Constraints:


	1 <= nums.length <= 105
	0 <= nums[i] <= 109

## Submission Details
- **Status**: Accepted
- **Runtime**: 34
- **Memory**: 34276000
- **Language**: python3

## Code
```python3
class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        if total_xor != 0:
            return len(nums)
            
        if has_nonzero:
            return len(nums) - 1
            
        return 0
```
