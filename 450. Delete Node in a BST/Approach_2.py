# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            successor = self.findMin(root.right)
            
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        """Helper function to find the minimum value node in a given tree."""
        current = node
        while current.left:
            current = current.left
        return current