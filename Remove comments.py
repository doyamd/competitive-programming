#
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        opened=False # the comments are closed
        temp=''
        res=[]
        
        for line in source:
            i=0
            while i<len(line):
                if line[i]=="/" and (i+1) != len(line) and line[i+1]=="/" and not opened:# in line comments open
                    break
                elif line[i]=="/" and (i+1) != len(line) and line[i+1]=="*" and not opened:# block comment opened
                    opened=True
                    i+=1
                elif line[i]=="*" and (i+1) != len(line) and line[i+1]=="/" and  opened:# block comment closed
                    opened=False
                    i+=1
                elif not opened:# appending to temp
                    temp += line[i]
                i+=1
            if temp and not opened:
                res.append(temp)
                temp=''

            
        return res
