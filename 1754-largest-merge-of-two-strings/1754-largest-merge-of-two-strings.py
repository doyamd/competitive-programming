class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = w2 = 0
        merge = ""
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1] > word2[w2]:
                merge += word1[w1]
                w1 +=1
            elif word1[w1] < word2[w2]:
                merge += word2[w2]
                w2 += 1
            else:
                if  word1[w1::] > word2[w2::]:
                    merge += word1[w1]
                    w1 += 1
                else: 
                    merge += word2[w2]
                    w2 += 1
            
        if w1 < len(word1):
            merge += word1[w1:]
        if w2 < len(word2):
            merge += word2[w2:]
        return merge