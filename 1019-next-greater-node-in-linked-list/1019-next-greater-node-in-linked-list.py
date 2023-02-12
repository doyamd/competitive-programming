# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        link = head
        nums = []
        ans = []
        stack = []
        while link:
            nums.append(link.val)
            ans.append(0)
            link =link.next
        i = 0
        while i < len(nums):
            val = nums[i]
            while stack and stack[-1][1] < val:
                index, value = stack.pop()
                ans[index] = val
            stack.append((i,val))
            i += 1
        return ans