#https://leetcode.com/problems/count-pairs-of-similar-strings/description/
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        unrepeated=[] # uprepeated letters in a list are stored
        for word in words:
            unrepeated.append(set(word))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if unrepeated[i]==unrepeated[j]: #if the pairs are similar they are counted
                    count+=1
        return count

                
