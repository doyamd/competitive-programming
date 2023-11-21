class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans=''
        wrd1_ptr=0
        wrd2_ptr=0
        while wrd1_ptr<len(word1) and wrd2_ptr<len(word2):
            ans=ans+word1[wrd1_ptr]
            ans=ans+word2[wrd2_ptr]
            wrd1_ptr+=1
            wrd2_ptr+=1

        if wrd1_ptr>=len(word1) and wrd2_ptr<len(word2):
                ans= ans+word2[wrd2_ptr:]
                
        else:
                ans=ans+word1[wrd1_ptr:]
        return ans
        
