# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        

        def sort(node1, node2):
            ans = ListNode(0)
            curr = ans 

            while node1 and node2:
                if node1.val <= node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next

            while node1:
                curr.next = node1
                node1 = node1.next
                curr = curr.next
            while node2:
                curr.next = node2
                node2 = node2.next
                curr = curr.next
            return ans.next
            
        def divide(node):
            if not node or not node.next:
                return node
            pre = None
            slow = node
            fast = node

            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next

            pre.next = None
            left = divide(node)
            right = divide(slow)

            return sort(left, right)

        

        return divide(node)