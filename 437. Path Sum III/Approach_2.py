from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = {0: 1}
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            paths_ending_here = prefix_sums.get(current_sum - targetSum, 0)
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
            total_paths = paths_ending_here \
                          + dfs(node.left, current_sum) \
                          + dfs(node.right, current_sum)
            prefix_sums[current_sum] -= 1
            
            return total_paths
            
        return dfs(root, 0)