class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = [False for _ in range(len(nums))]
        ans = []
        def backtracking(arr,flag):
            if all(flag):
                ans.append(arr[:])
                return
            for i in range(len(nums)):
                if not flag[i]:
                    flag[i] = True
                    arr.append(nums[i])
                    backtracking(arr,flag)
                    arr.pop()
                    flag[i] = False
        
        backtracking([],flag)
        return ans