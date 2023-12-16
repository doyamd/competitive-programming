class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        pos = []
        neg = []
        zero = False
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zero = True
        # print(pos,neg)
        def findStrength(pos,neg):
            positive,negative = 1,1
            if not pos and not neg:
                return 0
            if pos:
                positive = reduce(mul,pos)
            if neg:
                negative = reduce(mul,neg)
            
            return positive*negative
        # print(zero)
        if len(neg) % 2 == 0:
           return findStrength(pos,neg)
        elif len(neg) == 1 and not pos and zero:
            return 0
        elif len(neg) == 1 and not pos and not zero:
            return neg[0]
        elif len(neg) % 2 != 0:
            neg.sort()
            return findStrength(pos,neg[:len(neg)-1])
        