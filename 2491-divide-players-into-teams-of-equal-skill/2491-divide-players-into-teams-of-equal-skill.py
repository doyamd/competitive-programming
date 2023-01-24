class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 1 2 3 3 4 5
        skill.sort()
        i = 0
        j = len(skill)-1
        sums = 0
        orignal = skill[i]+skill[j]
        while i < j:
            prev = skill[i]+skill[j]
            sums += skill[i]*skill[j]
            if orignal != prev:
                return -1
            i += 1
            j -=1
        return sums
            