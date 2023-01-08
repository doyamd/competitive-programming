#
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        even=list(filter(lambda x:x%2==0, nums))
        sums=sum(even)#initial sum of evens
        for i in range(len(queries)):
            if nums[queries[i][1]]%2==0:
                sums=sums-nums[queries[i][1]]#minimizing if its even
            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]#performing the querie
            if nums[queries[i][1]]%2==0:
                sums=sums+nums[queries[i][1]]#adding it if its even
            ans.append(sums)
        if ans==[]:
            ans.append(0)
        return ans
