# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        list2 = slow.next
        slow.next = None

        prev = None

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp
        
        list2 = prev

        list1 = head

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next

            list1.next = list2
            list2.next = temp1

            list1 = temp1
            list2 = temp2