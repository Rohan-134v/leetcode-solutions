# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        thing, fast, slow = [], head, head
        while fast:
            fast=fast.next.next
            thing.append(slow.val)
            slow=slow.next
        fast=0
        for n in thing[::-1]:
            n+=slow.val
            slow=slow.next
            if n > fast:
                fast = n
        return fast