#https://leetcode.com/problems/goal-parser-interpretation/description/
class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        indx=0
        ans=''
        while indx<len(command):
            if(command[indx]=='(' and command[indx+1]==')'):
                ans=ans+'o'
                indx+=2
            elif(command[indx]=='(' and command[indx+1]=='a'):
                ans=ans+'al'
                indx+=4
            elif(command[indx]=='G'):
                ans=ans+'G'
                indx+=1
        return ans
