class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = [i for i in range(1,arr[-1]+1)]
        count = 0
        for i in nums:
            if i not in arr:
                count += 1
            if count == k:
                return i
        return len(arr) + k


        