class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxi = len(nums)
        ans = []
        arr = [-1 for _ in range(maxi)]
        for i in nums:
            arr[i-1] = i
        for i in range(len(arr)):
            if arr[i] == -1:
                ans.append(i+1)
        return ans