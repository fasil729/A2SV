# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        q = 0
        while l1 or l2:
            if l1:
                if l2:
                     sum = l1.val + l2.val + q
                     curr.next = ListNode(sum % 10)
                     q = sum // 10
                     l2 = l2.next
                else:
                     curr.next = ListNode((l1.val + q) % 10)
                     q = (l1.val + q) // 10
                l1 = l1.next     
            elif l2:
                curr.next = ListNode((l2.val + q) % 10)
                q = (l2.val + q) // 10
                l2 = l2.next
            curr = curr.next
        if q:
            curr.next = ListNode(q)
        return dummy.next