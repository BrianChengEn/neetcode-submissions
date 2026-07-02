# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        head2 = head

        while head2 and head2.next:
            head = head.next
            head2 = head2.next.next
            if head == head2:
                return True
        
        return False