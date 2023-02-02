# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        link = head
        arr = []
        while link:
            arr.append(link.val)
            link = link.next
        i = 0
        j = i+k-1
        while j < len(arr):
            front = i
            back = j
            while front < back:
                arr[front], arr[back] = arr[back], arr[front]
                front += 1
                back -= 1
            i = j+1
            j = i+k-1
        link = head
        i = 0
        while link:
            link.val = arr[i]
            link = link.next
            i += 1
        return head