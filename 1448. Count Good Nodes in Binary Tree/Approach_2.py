# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        maxi = root.val
        stack = [[root,maxi]]
        
        while stack:
            node, maxi = stack.pop()
            if node:
                if maxi <= node.val:
                    maxi = node.val
                    good += 1
                stack.append([node.right, maxi])
                stack.append([node.left, maxi])
        return good

            
