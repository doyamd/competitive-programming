# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        ans = ListNode()
        tail = ans
        
        if not head or not head.next:
            return head
        while ptr and ptr.next:
            tail.next = ListNode()
            tail.next.val = ptr.val
            ptr = ptr.next.next
            tail = tail.next
        if ptr:
            tail.next = ListNode()
            tail.next.val =ptr.val
            tail = tail.next
        #print(ptr.val) 
        ptr = head.next
        while ptr and ptr.next:
            tail.next = ListNode()
            tail.next.val = ptr.val
            ptr = ptr.next.next
            tail = tail.next
        if ptr:
            tail.next = ListNode()
            tail.next.val =ptr.val
            tail = tail.next
      
            
        return ans.next
            