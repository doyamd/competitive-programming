class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i != '*':
                ans.append(i)
            else:
                del ans[-1]
        ans = "".join(ans)
        return ans