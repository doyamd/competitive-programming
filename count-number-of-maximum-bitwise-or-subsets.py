class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
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
        d = defaultdict(int)
        maxi = 0
        for i in range(len(ans)):
            _or = 0
            for j in ans[i]:
                _or |=j 
            maxi = max(maxi,_or)
            d[i] = _or 
        count = 0
        for k,v in d.items():
            if v == maxi:
                count += 1
    
        return count