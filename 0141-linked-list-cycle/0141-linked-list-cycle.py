# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head  and head.next:
            fast = head.next.next
            slow = head
            while fast != slow and fast and fast.next :
                slow = slow.next
                fast = fast.next.next
            if not fast or not fast.next  :
                return False
            else:
                return True
        else:
            return False
            