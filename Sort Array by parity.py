#https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        while i<n:
            if nums[i] %2 !=0:
               no=nums.pop(i)
               nums.append(no)
               n-=1
               i-=1
            i+=1
        return nums
        
