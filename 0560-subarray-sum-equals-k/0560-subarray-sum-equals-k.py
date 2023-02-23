class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = 0
        
        d = defaultdict(int)
        d[0] = 1
        for i in nums:
            pre += i
            ans += d[pre-k]
            d[pre] += 1 
        return ans
                
            
                
        
        
            
    
            
                