class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d = defaultdict(int)
        for i in equations:
            d[i[0]] = i[0]
            d[i[3]] = i[3]
        for i in equations:
            if i[1]+i[2] == "==":
                temp = d[i[3]]
                for k,v in d.items():
                    if v == temp:
                        d[k] = d[i[0]]
        for i in equations:
            if i[1]+i[2] == "!=" and d[i[3]] == d[i[0]]:
                return False
        return True