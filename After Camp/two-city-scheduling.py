class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2
        cost1 = sorted(costs, key = lambda x:(abs(x[0]-x[1])), reverse=True)
        print(cost1)
        a,b = N,N
        total = 0
        for city1, city2 in cost1:
            if city1 < city2:
                if a:
                    a -= 1 
                    total += city1
                else:
                    b -= 1
                    total += city2
            else:
                if b:
                    b -= 1 
                    total += city2
                else:
                    a -= 1
                    total += city1
            print(total, city1)
        return total


            