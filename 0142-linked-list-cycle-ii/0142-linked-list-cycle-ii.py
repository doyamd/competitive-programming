# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = True
        if head  and head.next:
            fast = head.next.next
            slow = head.next
            while fast != slow and fast and fast.next :
                slow = slow.next
                fast = fast.next.next
            if not fast or not fast.next  :
                flag = False
        else:
            flag = False
        if flag:
            inner = slow
            while head != inner:
                head = head.next
                inner = inner.next
            return head   
             