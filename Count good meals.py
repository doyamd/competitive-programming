#https://leetcode.com/problems/count-good-meals/description/
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        good_meals=0
        food=defaultdict(int)

        for i in deliciousness:
            for j in range(23):# powers of 2
                meal=(2**j)-i
                if meal in food:
                   good_meals+=food[meal]
            food[i]+=1
        return (good_meals%(10**9+7))

                
