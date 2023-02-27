class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        rang = k
        x = 0
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                odds.append(i)
        odds.append(len(nums))
        for right in range(len(nums)):
            if nums[right] % 2!= 0:
                rang -= 1
                x += 1
                
            while left <= right and rang == 0:
                temp = 1 + odds[x]- right
         
                if nums[right] %2 != 0:
                    temp = 1 + odds[x] - right -1
                ans += temp
                if nums[left] % 2!= 0:
                    rang += 1
                    right += 1
                left += 1
        return ans
                    