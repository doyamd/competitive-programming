class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = [0]*26
        d2 = [0]*26
     
        if len(s2) < len(s1):
            return False
        match = 0
        for i in s1:
            d1[(ord(i)-ord('a'))] += 1
        for i in s2[:len(s1)]:
            d2[(ord(i)-ord('a'))] += 1
        for i in range(26):
            if d1[i] == d2[i]:
                match += 1
        # print(match)
        j = 0
        for i in range(len(s1),len(s2)):
            # print(s2[i],match,s2[j])
            if match == 26:
                return True
            letter1 = (ord(s2[j])-ord('a'))
            letter2 = (ord(s2[i])-ord('a'))
            if d2[letter1] == d1[letter1]:
                match -= 1
                d2[letter1] -= 1
            else:
                d2[letter1] -= 1
                if d2[letter1] == d1[letter1]:
                    match += 1

           
            if d2[letter2] == d1[letter2]:
                match -= 1
                d2[letter2] += 1
            else:
                d2[letter2] += 1
                if d2[letter2] == d1[letter2]:
                    match += 1
            j += 1
        if match == 26:
            return True
        return False