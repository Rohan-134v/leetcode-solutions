# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        max_sum = 0
        first_head = head
        second_head = prev

        while second_head:
            twin_sum = first_head.val + second_head.val
            max_sum = max(max_sum, twin_sum)
            first_head = first_head.next
            second_head = second_head.next

        return max_sum




