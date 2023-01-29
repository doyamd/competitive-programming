# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    #None<- 1 <- 2 <- 3  4 -> 5 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        aft = None
        prev = None
        if not head:
            return head
        
        while curr.next != None:
            aft = curr.next
            curr.next = prev
            prev = curr
            curr = aft
            
        curr.next = prev
        head = curr
        return head