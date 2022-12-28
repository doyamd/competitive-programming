#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        count=0
        for i in range(nums.count(0)):
           nums.remove(0)
           count+=1
        while count>0:
            nums.append(0)
            count-=1
         '''
        indx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[indx]=nums[i]
                indx+=1
        for j in range(indx,len(nums)):
            nums[j]=0
               
            
