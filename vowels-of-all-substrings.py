class Solution:
    def countVowels(self, word: str) -> int:
        vow = {'a','e','i','o','u'}
        n = len(word)
        ans = 0
        for i in range(n):
            if word[i] in vow:
                ans += (i+1) * (n-i)
        return ans