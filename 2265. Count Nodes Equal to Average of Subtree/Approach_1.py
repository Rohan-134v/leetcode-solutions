# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return 0,0

            leftSum, leftcount = dfs(node.left)
            rightSum, rightcount = dfs(node.right)

            currentSum = node.val + leftSum + rightSum
            currentCount = 1 + leftcount + rightcount

            if currentSum // currentCount == node.val:
                self.count += 1

            return currentSum, currentCount  
        dfs(root)
        return self.count