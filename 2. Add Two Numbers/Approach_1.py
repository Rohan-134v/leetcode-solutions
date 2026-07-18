# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem=0
        sum = ListNode()
        res=sum
        while l1 or l2 or rem:
            total = rem
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next

            num=total%10
            rem=total//10
            sum.next=ListNode(num)
            sum=sum.next
        return res.next


        
        