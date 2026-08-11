# 437. Path Sum III

### Difficulty: Medium

## Description
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 
Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.


Example 2:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


 
Constraints:


	The number of nodes in the tree is in the range [0, 1000].
	-109 <= Node.val <= 109
	-1000 <= targetSum <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 176
- **Memory**: 19924000
- **Language**: python3

## Code
```python3
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        stack = [(root, [])]
        count = 0 

        while stack:
            node, parent_sums = stack.pop()
            
            if node:
                current_sums = [s + node.val for s in parent_sums]
                current_sums.append(node.val)
                for s in current_sums:
                    if s == targetSum:
                        count += 1
                if node.right:
                    stack.append((node.right, current_sums))
                if node.left:
                    stack.append((node.left, current_sums))
            print(parent_sums)
                    
        return count
```
