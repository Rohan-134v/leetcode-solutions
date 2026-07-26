# 628. Maximum Product of Three Numbers

### Difficulty: Easy

## Description
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 
Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [1,2,3,4]
Output: 24
Example 3:
Input: nums = [-1,-2,-3]
Output: -6

 
Constraints:


	3 <= nums.length <= 104
	-1000 <= nums[i] <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 23
- **Memory**: 20416000
- **Language**: python3

## Code
```python3
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = len(nums)
        op1 = nums[0] * nums[1] * nums[a - 1]
        op2 = nums[a - 1] * nums[a - 2] * nums[a - 3]
        return max(op1, op2)
```
