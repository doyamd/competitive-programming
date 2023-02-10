# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        head = ListNode()
        tail = head
        add = 0
        sums = 0
        while list1 and list2:
            tail.next = ListNode()
            sums = list1.val + list2.val + add
            if sums <= 9:
                add = 0
                tail.next.val = sums
            else:
                x = str(sums)
                add = sums//10
                tail.next.val = int(x[-1])
            tail = tail.next
            list1 = list1.next
            list2 = list2.next
        while list1:
            tail.next = ListNode()
            sums = list1.val + add
            if sums <= 9:
                add = 0
                tail.next.val = sums
            else:
                x = str(sums)
                add = sums//10
                tail.next.val = int(x[-1])
            tail = tail.next
            list1 = list1.next
        while list2:
            tail.next = ListNode()
            sums = list2.val + add
            if sums <= 9:
                add = 0
                tail.next.val = sums
            else:
                x = str(sums)
                add = sums//10
                tail.next.val = int(x[-1])
            tail = tail.next
            list2 = list2.next
        if add > 0:
            tail.next = ListNode()
            tail.next.val = add
        return head.next
    
        
        
        