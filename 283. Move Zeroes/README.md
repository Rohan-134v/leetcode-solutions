# 283. Move Zeroes

### Difficulty: Easy

## Description
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:


	1 <= nums.length <= 104
	-231 <= nums[i] <= 231 - 1


 
Follow up: Could you minimize the total number of operations done?

## Submission Details
- **Status**: Accepted
- **Runtime**: 7
- **Memory**: 20420000
- **Language**: python3

## Code
```python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wp = 0

        for rp in range(len(nums)):
            if nums[rp] != 0:
                nums[rp], nums[wp] = nums[wp], nums[rp]
                wp += 1
 
```
