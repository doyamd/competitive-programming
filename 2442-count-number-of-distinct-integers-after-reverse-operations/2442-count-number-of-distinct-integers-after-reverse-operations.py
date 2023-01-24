class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            x = str(nums[i])
            reversed(x)
            x = int("".join(reversed(x)))
            nums.append(x)
        distnict = set(nums)
        return len(distnict)