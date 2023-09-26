class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        if len(scores) == 1:
            return scores[0]
        arr = sorted(zip(scores,ages))
        memo = [arr[i][0] for i in range(len(scores))]
        
        for i in range(len(scores)):
            mscore,mage = arr[i]
            for j in range(i):
                score,age = arr[j]
                if mage >= age:
                    memo[i] = max(memo[i], mscore + memo[j])
            
        return max(memo)