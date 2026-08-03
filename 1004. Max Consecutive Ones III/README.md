# 1004. Max Consecutive Ones III

### Difficulty: Medium

## Description
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 
Example 1:


Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:


Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


 
Constraints:


	1 <= nums.length <= 105
	nums[i] is either 0 or 1.
	0 <= k <= nums.length

## Submission Details
- **Status**: Accepted
- **Runtime**: 51
- **Memory**: 22364000
- **Language**: python3

## Code
```python3
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        maximum_bin = 0
        zeros = 0

        for last in range(len(nums)):
            if nums[last] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[start] == 0:
                    zeros -= 1
                start +=  1
            
            maximum_bin = max(maximum_bin, last - start + 1)
        
        return maximum_bin

```
