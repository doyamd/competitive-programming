class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        d = []
        maxi = 0
        words.sort()
        for word in words:
            
            if len(word) == 1:
                d.append(word)
                maxi = max(maxi,len(word))
            else:
                if word[:-1] in d:
                    d.append(word)
                    maxi = max(maxi, len(word))
        ans = ''
        for w in d:
            if len(w) == maxi:
                if not ans:
                    ans = w
                ans = min(ans,w)
        return ans