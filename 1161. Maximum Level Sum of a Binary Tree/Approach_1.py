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
            

