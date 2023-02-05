# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ptr = head.next
        mini = head
        while curr:
            ptr = curr.next
            while ptr:
                if mini.val > ptr.val:
                    mini = ptr
                ptr = ptr.next
            mini.val, curr.val = curr.val, mini.val
            curr = curr.next
            mini = curr
            
        return head