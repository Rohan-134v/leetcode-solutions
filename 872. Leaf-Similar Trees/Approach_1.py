# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        def leaf(root: Optional[TreeNode], leafnode:Optional[TreeNode]):
            stack = [root]
            while stack:
                node = stack.pop()
                if node:
                    if node.right or node.left:
                        stack.append(node.left)
                        stack.append(node.right)
                    else:
                        leafnode.append(node.val)
        
        leaf(root1, leaf1)
        leaf(root2, leaf2)
        print(leaf1)
        print(leaf2)

        return leaf1 == leaf2
                


