class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        d = defaultdict(int)
        ans = 0
        for i in range(len(s)):
            for j in range(len(s)-1,i-1,-1):
                if s[i] == s[j]:
                    if i == j:
                        d[(i,j)] = 1
                    else:
                        d[(i,j)] = 2
                    if i-1 >=0:
                        d[(i,j)] += d[(i-1,j+1)]
                else:
                    d[(i,j)] = d[(i,j+1)]
                    if i-1 >= 0:
                        d[(i,j)] = max(d[(i,j)],d[(i-1,j)])
                ans = max(ans,d[(i,j)])
        return ans