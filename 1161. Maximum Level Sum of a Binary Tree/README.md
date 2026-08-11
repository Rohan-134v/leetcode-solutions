# 1161. Maximum Level Sum of a Binary Tree

### Difficulty: Medium

## Description
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 
Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


Example 2:


Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


 
Constraints:


	The number of nodes in the tree is in the range [1, 104].
	-105 <= Node.val <= 105

## Submission Details
- **Status**: Accepted
- **Runtime**: 23
- **Memory**: 22748000
- **Language**: python3

## Code
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, level, ans = float('-inf'), 0, 0
        
        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sum_at_curr_lvl = 0

            for _ in range(len(q)):
                node = q.popleft()
                sum_at_curr_lvl += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if max_sum < sum_at_curr_lvl:
                max_sum, ans = sum_at_curr_lvl, level
            
        return ans
            


```
