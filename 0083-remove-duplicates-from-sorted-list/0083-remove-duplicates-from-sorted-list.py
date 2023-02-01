# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            fast = head.next
            slow = head
            while fast :
                while fast and slow.val == fast.val :
                    fast = fast.next
                slow.next = fast
                slow = fast
                if fast:
                    fast = fast.next
        return head
