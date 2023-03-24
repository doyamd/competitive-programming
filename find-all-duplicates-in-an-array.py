class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        maxi = len(nums)
        ans = []
        arr = [0 for _ in range(maxi)]
        print(arr)
        for i in nums:
            arr[i-1] += i
        for i in range(len(arr)):
            if arr[i] == (i+1)*2:
                ans.append(i + 1)
        return ans