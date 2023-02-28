class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = list(s)
        maxi = 0
        path = [0 for i in range(len(s))]
        
        for i in range(len(shifts)):
                if shifts[i][2] == 0:
                    path[shifts[i][0]] += -1
                    if shifts[i][1]+1 < len(path):
                        path[shifts[i][1]+1] += 1
                else:
                    path[shifts[i][0]] += 1
                    if shifts[i][1]+1 < len(path):
                        path[shifts[i][1]+1] += -1
                
        for i in range(len(path)):
            if i != 0:
                path[i] += path[i-1]
            if path[i] + ord(arr[i]) < 97:
                sub =(ord(arr[i]) - ord('a') + path[i])%26
                arr[i] = chr(sub + ord('a'))
            elif path[i] + ord(arr[i]) > 122:
                sub = (path[i] + ord(arr[i])-ord('a'))%26
                arr[i] = chr(sub+ord('a'))
            else:
                arr[i] = chr(path[i] + ord(arr[i]))
        
        return "".join(arr)