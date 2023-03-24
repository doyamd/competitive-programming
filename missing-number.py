class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = len(nums)
        arr = [-1 for _ in range(maxi + 1)]
        for i in nums:
            arr[i] = i
            
        return arr.index(-1)