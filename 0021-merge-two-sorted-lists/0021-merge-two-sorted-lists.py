# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, link1: Optional[ListNode], link2: Optional[ListNode]) -> Optional[ListNode]:
        link = ListNode()
        head = link
        l1 = link1
        l2 = link2
        while l1 and l2:
            link.next = ListNode()
            link = link.next
            if l1.val <= l2.val:
                link.val = l1.val
                l1 = l1.next
            else:
                link.val = l2.val
                l2 = l2.next
            
        if l1:
            while l1:
                link.next = ListNode()
                link = link.next
                link.val = l1.val
                l1 = l1.next
        elif l2:
            while l2:
                link.next = ListNode()
                link = link.next
                link.val = l2.val
                l2 = l2.next
            
            
            
        return head.next
            
        