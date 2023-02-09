# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        link = head
        arr = []
        while link:
            arr.append(link.val)
            link = link.next
        i = 0
        j = len(arr)-1
        maxi = 0
        while i < j:
            sums = arr[i] + arr[j]
            maxi = max(maxi, sums)
            i += 1
            j -= 1
        return maxi