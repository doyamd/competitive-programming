#https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
      #keeping our count of words in a-z format
        first_word=[0]*26 
        other_word=[0]*26
        common_letters=[]
        letter=ord('a')
        for i in words[0]:
            indx=ord(i)-letter
            first_word[indx]+=1
        i=1
        while i<len(words):
            itter=0
            for j in words[i]:
                indx=ord(j)-letter
                other_word[indx]+=1
            while itter<26:
                first_word[itter]=min(first_word[itter],other_word[itter])
                itter+=1
            other_word=[0]*26
            i+=1
        itter=0
        while itter<26:
            if first_word[itter]!=0:
                j=0
                while j<first_word[itter]:
                    char=chr(itter+letter)
                    common_letters.append(char)
                    j+=1
            itter+=1
        return common_letters
