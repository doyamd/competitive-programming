# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        link = head
        i = 0
        size = 0
        while link.next != None:
            link = link.next
            size += 1
        link = head
        indx = size - n
        if head.next == None:
            head = None
        else:
            while i < indx:
                link = link.next
                i += 1
            if indx == -1:
                #print(head.val)
                head = head.next
            elif link.next.next == None:
                link.next = None
            
            else:
                link.next = link.next.next
        
        return head
        