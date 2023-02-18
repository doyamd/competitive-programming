# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new = ListNode()
        new.next = head
        header = new
        curr = head
        l1 = head
        l2 = head.next
        while l1 and l2:
            curr = l2.next
            header.next = l2
            l2.next = l1
            l1.next =None
            header = l1
            l1 = curr
            if curr:
                l2 = curr.next
        if curr:
            header.next = curr
            
        return new.next
            

        #0 -> 2 -> 1 -> 4 -> 3