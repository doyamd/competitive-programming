#https://leetcode.com/problems/apply-operations-to-an-array/
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                i+=1
            i+=1
        indx=0
        #moving the zeros
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[indx]=nums[i]
                indx+=1
        for j in range(indx,len(nums)):
            nums[j]=0
        return nums
