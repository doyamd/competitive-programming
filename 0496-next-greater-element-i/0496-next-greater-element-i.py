class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        ans = []
        for i in nums2:
            if not stack or stack[-1] > i:
                stack.append(i)
            elif stack[-1] < i:
                while stack and stack[-1] < i:
                    d[stack[-1]] = i
                    stack.pop()
                stack.append(i)
        while stack :
            if stack[-1] not in d:
                d[stack[-1]] = -1
                stack.pop()
        for i in nums1:
            ans.append(d[i])
        return ans
                