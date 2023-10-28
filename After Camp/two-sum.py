class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        ans = [0,0]

        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            
            if (target - nums[i] ) in d and d[target - nums[i]] != i:
                ans[0] = d[target - nums[i]]
                ans[1] = i
                break   
        return ans

