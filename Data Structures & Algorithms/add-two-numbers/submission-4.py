# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1.val and not l2.val:
            node = ListNode()
            return node
        n1 = 0
        n2 = 0

        d1 = 0
        d2 = 0

        while l1:
            n1 += (10 ** d1) * l1.val
            l1 = l1.next
            d1 += 1
        
        while l2:
            n2 += (10 ** d2) * l2.val
            l2 = l2.next
            d2 += 1
        
        num = n1 + n2

        dummy = ListNode()
        curr = dummy

        while num:
            curr.next = ListNode(val = (num % 10), next = None)
            num = num // 10
            curr = curr.next
        
        return dummy.next