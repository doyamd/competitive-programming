# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        link = head
        if head == None:
            return head
        if head.next == None:
            return head
        while link.next != None:
            link = link.next
            count += 1
        
        k = k%count
        for i in range(k):
            link = head
            while link.next.next != None:
                link = link.next
            temp = link.next
            link.next = None
            temp.next = head
            head = temp
        return head
                