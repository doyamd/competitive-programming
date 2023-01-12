class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        flag=True
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i]>strs[j+1][i]:
                    flag=False
            if not flag:
                count+=1
                flag=True
                    
        return count