class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        j = 1
        ans = 0
        greater = True
        less = True
        while j < len(arr):
            if arr[j-1] > arr[j] and less:
                greater = True
                less = False
                j += 1
            elif arr[j-1] < arr[j] and greater:
                less = True
                greater = False 
                j += 1
            else:
                if arr[j-1] == arr[j]:
                    i = j
                    j += 1
                else:
                    i =j - 1
                greater = True
                less = True
            ans = max(ans, j-i)
        ans = max(ans, j-i)
        return ans