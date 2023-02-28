# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        head  = None
        tail = None
        
        def merge(l1, l2):
            
            nonlocal head, tail
            #print(l1.val if l1 else None, l2.val if l2 else None)
            if not l1 and not l2:
                return 
            
            temp = 0
            exist = True
            if not l1:
                temp = l2.val
                l2 = l2.next
                exist = False
            if exist and  not l2:
                temp = l1.val
                l1 = l1.next
                exist = False
            
            if exist:
                if l1.val > l2.val:
                    temp = l2.val
                    l2 = l2.next
                else:
                    temp = l1.val
                    l1 = l1.next
            
            node = ListNode(temp)
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
                
            merge(l1, l2)
        
        merge(list1, list2)
        return head