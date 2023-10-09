class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        arr = [[-1]*len(nums2) for _ in range(len(nums1))]
        def dp(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if arr[i][j] == -1:
                if nums1[i] == nums2[j]:
                    arr[i][j] = 1+dp(i+1,j+1)
                else:
                    arr[i][j] = max(dp(i+1,j),dp(i,j+1))
            return arr[i][j]
        return dp(0,0)