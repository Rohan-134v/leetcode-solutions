# 905. Sort Array By Parity

### Difficulty: Easy

## Description
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 
Example 1:


Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Example 2:


Input: nums = [0]
Output: [0]


 
Constraints:


	1 <= nums.length <= 5000
	0 <= nums[i] <= 5000

## Submission Details
- **Status**: Accepted
- **Runtime**: 2
- **Memory**: 19584000
- **Language**: python3

## Code
```python3
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        read = 0
        write = len(nums) - 1
        
        while read < write:
            if nums[read] % 2 != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write -= 1
            else:
                read += 1
        return nums
```
