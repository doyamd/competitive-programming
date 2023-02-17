# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h1 = headA
        h2 = headB
        c1 = 0
        c2 = 0
        while h1:
            c1 +=1
            h1 = h1.next
        while h2:
            c2 +=1
            h2 = h2.next
        h1 = headA
        h2 = headB
        if c1 > c2:
            itter = c1-c2
            while itter != 0:
                h1 = h1.next
                itter -= 1
        if c2 > c1:
            itter = c2-c1
            while itter != 0:
                h2 = h2.next
                itter -= 1
        while h1 and h2 and h1!=h2:
            h1 = h1.next
            h2 = h2.next
        return h1
            