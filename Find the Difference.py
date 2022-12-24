#https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans=''
        if len(s)==0:
            return t
           
        new_t=''.join(sorted(t))
        new_s=''.join(sorted(s))
        s_ptr=0
        t_ptr=0
        while s_ptr<len(s) and t_ptr<len(t):
            if new_s[s_ptr]!=new_t[t_ptr]:
                ans=new_t[t_ptr]
                break
            s_ptr+=1
            t_ptr+=1
        if ans=='':
            ans=new_t[len(t)-1]
        return ans
