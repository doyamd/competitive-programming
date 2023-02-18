# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        i = head
        j = head.next
        while i and j:
            i.val, j.val = j.val, i.val
            if i.next and j.next:
                i = j.next
                j = i.next
            else:
                break
        return head
        