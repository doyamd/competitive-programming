class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        d = defaultdict(int)
        ans = 0
        maxi = 0
        for j in range(len(s)):
            d[s[j]] += 1
            maxi = max(maxi,d[s[j]])
            while (j - i+ 1 - maxi) > k:
                d[s[i]] -= 1
                i += 1
            ans = max(ans,j-i+1)
        return ans
        