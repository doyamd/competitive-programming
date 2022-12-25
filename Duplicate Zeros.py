#
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n= len(arr)
        indx=0
        while indx+1<n:
            if arr[indx]==0:
                j=n-1
                while j>indx:
                    arr[j]=arr[j-1]
                    arr[j-1]=0
                    j-=1
                indx+=1
            indx+=1
                   
