# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        node = l1
        while node:
            num1 += str(node.val)
            node = node.next
        node = l2
        while node:
            num2 += str(node.val)
            node = node.next
        ans = str(int(num1)+int(num2))
        dummy = ListNode()
        ptr = dummy
        for i in ans:
            temp = ListNode(val=int(i))
            ptr.next = temp
            ptr = ptr.next
        return dummy.next