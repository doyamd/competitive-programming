class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            x = str(nums[i])
            reversed(x)
            x = int(x[::-1])
            nums.append(x)
        distnict = set(nums)
        return len(distnict)