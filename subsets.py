class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(indx,arr):
            nonlocal ans
            if len(arr) == len(nums) :
                ans.append(arr)
                return 
        
            ans.append(arr)
            
            for i in range(indx,len(nums)):
                backtrack(i+1, arr + [nums[i]])

        # for i in range(len(nums)):
        backtrack(0,[])
        return ans