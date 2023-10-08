class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        n = len(gas)
        tot = 0
        if sum(cost) > sum(gas):
            return -1
        for i in range(n):
            tot += gas[i] - cost[i]
            if tot < 0:
                start = i + 1
                tot = 0
        return start