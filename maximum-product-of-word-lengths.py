class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0
        lett = [set(w) for w in words]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if lett[i].isdisjoint(lett[j]):
                    maxi = max(maxi,(len(words[i])*len(words[j])))
        return maxi