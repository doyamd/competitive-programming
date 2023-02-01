# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            last = head
            first = head
            link = head
            temp =[]
            count = 1
            left = left-1
            right = right-1
            while link:
                temp.append(link.val)
                link = link.next
            while left < right:
                temp[right], temp[left] = temp[left], temp[right]
                right -= 1
                left += 1
            link = head
            i = 0
            
            while link:
                link.val = temp[i]
                link = link.next
                i += 1
            return head
                