# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        link = head
        rev = []
        while link:
            rev.append(link.val)
            link = link.next
        i = 0
        j = len(rev)-1
        while i < j:
            rev[i], rev[j] = rev[j], rev[i]
            i += 1
            j -= 1
        i = 0
        link = head
        while link:
            if link.val != rev[i]:
                return False
            i += 1
            link = link.next
        return True
      