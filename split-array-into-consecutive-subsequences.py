class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
            
        i = 0
        while i < len(nums):
            
            if freq[nums[i]] == 0:
                i +=1 
                continue
            if d[nums[i]-1] > 0:
                d[nums[i]-1] -= 1
                d[nums[i]] += 1
                freq[nums[i]] -= 1
                
            elif freq[nums[i]+1] > 0 and freq[nums[i]+2] > 0:
                freq[nums[i]+1] -= 1
                freq[nums[i]+2] -= 1
                freq[nums[i]] -= 1
                d[nums[i]+2] += 1
            else:
                return False

            i +=1     
        return True