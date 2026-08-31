# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        first_idx = -1
        curr_idx = 1
        prev_idx = -1
        last_idx = -1

        min_dist = float('INF')

        while curr.next:
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val

            if is_maxima or is_minima:
                if first_idx == -1:
                    first_idx = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx-prev_idx)
                    
                prev_idx = curr_idx
            
            prev = curr
            curr = curr.next
            curr_idx += 1
        
        if min_dist == float('INF'):
            return [-1,-1]

        return [min_dist,(prev_idx-first_idx)]
                 
                          