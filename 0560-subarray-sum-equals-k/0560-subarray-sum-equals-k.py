class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = []
        pre.append(nums[0])
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        d = defaultdict(int)
        d[0] = 1
        
        for i in pre:
            ans += d[i-k]
            d[i] += 1 
        return ans
                
            
                
        
        
            
    
            
                