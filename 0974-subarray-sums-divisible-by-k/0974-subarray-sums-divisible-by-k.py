class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(int)
        d[0] += 1
        pre = 0
        
        for i in nums:
            pre += i
            ans += d[pre%k]
            d[pre%k] += 1
        return ans
    
    
    