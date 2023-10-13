class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        j = 0
        ans = 0
        for i in range(len(rating)):
            l_great,l_less = 0,0
            r_great,r_less = 0,0
            j = i-1
            while j > -1:
                if rating[i] > rating[j]:
                    l_less += 1
                if rating[i] < rating[j]:
                    l_great += 1
                j -= 1
            j = i+1
            while j < len(rating):
                if rating[i] > rating[j]:
                    r_less += 1
                if rating[i] < rating[j]:
                    r_great += 1
                j += 1
            ans += (l_less*r_great)+(l_great*r_less)
        return ans