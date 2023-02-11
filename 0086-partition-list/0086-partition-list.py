# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        link = head
        vals = []
        while link :
            if link.val < x:
                vals.append(link.val)
            link = link.next
        link = head
        while link:
            if link.val >= x:
                vals.append(link.val)
            link = link.next
        link = head
        for i in vals:
            link.val = i
            link = link.next
        return head