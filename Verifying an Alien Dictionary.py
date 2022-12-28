#
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict={}
        for i,letter in enumerate(order):
            alien_dict[letter]=i
        def comp(wrd1,wrd2):
          
            mini=min(len(wrd1),len(wrd2))
            for i in range(mini):
                if alien_dict[wrd1[i]]>alien_dict[wrd2[i]]:
                    return False
                if alien_dict[wrd1[i]]<alien_dict[wrd2[i]]:
                    return True
            if len(wrd2)<len(wrd1):
                return False
            return True
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not comp(words[i],words[j]):
                    return False
        return True
