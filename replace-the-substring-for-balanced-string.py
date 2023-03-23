class Solution:
    def balancedString(self, s: str) -> int:
        d = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for i in s:
           d[i] += 1
        flag = False
        num = len(s) // 4
        
        wanted = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for i in d:
            if d[i] > num:
                flag = True
                wanted[i] = d[i] - num
        if not flag:
            return 0
        slider = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        j = 0 
        i = 0
        ans = len(s)
        def isnotgreat(slider, wanted):
            for x in slider:
                if slider[x] < wanted[x]:
                    return False
            return True
        while j < len(s):
            slider[s[j]] += 1
            j += 1
            while isnotgreat(slider, wanted):
                ans = min(ans, j - i)
                slider[s[i]] -= 1
                i += 1
        return ans