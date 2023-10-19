class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = set()
        sums.add(0)
        if sum(nums)%2:
            return False
       
        target = sum(nums)//2
        curr_sum = 0
        for i in range(len(nums)):
            temp = set()
            for j in sums:
                if nums[i]+j == target:
                    return True
                temp.add(nums[i]+j)
            sums.update(temp)

        if target in sums:
            return True
        return False