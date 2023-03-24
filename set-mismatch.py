class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        maxi = len(nums)
        arr = [0 for _ in range(maxi)]
        dup = 0
        miss = 0
        for i in nums:
            arr[i-1] += i
        print(arr)
        for i in range(len(arr)):
            if arr[i] == (i+1)*2 :
                dup = i + 1
            if arr[i] == 0:
                miss = i + 1
        return [dup,miss]