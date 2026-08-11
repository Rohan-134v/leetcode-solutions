# 53. Maximum Subarray

### Difficulty: Medium

## Description
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 
Example 1:


Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Example 2:


Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.


Example 3:


Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


 
Constraints:


	1 <= nums.length <= 105
	-104 <= nums[i] <= 104


 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Submission Details
- **Status**: Accepted
- **Runtime**: 27
- **Memory**: 31532000
- **Language**: python3

## Code
```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_global = max_current = nums[0] 
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current
        return max_global
```
