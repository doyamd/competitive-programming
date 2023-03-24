class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maxi = len(nums)
        arr = [0 for _ in range(maxi)]
        
        for i in nums:
            arr[i-1] += i
        print(arr)
        for i in range(len(arr)):
            if arr[i] > i + 1 :
                return i + 1