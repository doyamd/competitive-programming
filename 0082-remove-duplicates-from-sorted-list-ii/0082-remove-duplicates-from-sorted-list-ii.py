# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        front = ListNode 
        front.next = head
        retrn = front
        while curr:
            if curr and curr.next and curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                front.next = curr.next  
            else:
                front = front.next
            curr = curr.next
        return retrn.next