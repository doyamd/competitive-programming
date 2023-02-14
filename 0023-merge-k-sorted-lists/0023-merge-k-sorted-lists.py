# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        i = 0
        while i < len(lists):
            ptr = lists[i]
            while ptr:
                arr.append(ptr.val)
                ptr = ptr.next
            i +=1
        arr.sort()
        i = 0
        head = ListNode()
        tail = head
        while i < len(arr):
            tail.next = ListNode()
            tail.next.val = arr[i]
            tail = tail.next
            i += 1
        return head.next