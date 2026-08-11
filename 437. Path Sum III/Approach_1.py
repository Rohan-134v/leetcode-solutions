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