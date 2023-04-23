class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        i = 0 
        j = 0
        count = 0
        for i in range(len(nums)):
            gd = nums[i]
            if gd == k:
                count += 1
            for j in range(i+1,len(nums)):
                gd = gcd(gd,nums[j])
                if gd == k:
                    count += 1
                elif gd < k:
                    break
        return count