class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ismountain = False
        dec=0
        inc=0
        if len(arr)<3:
            return ismountain
        else:
            maxi = max(arr)
            i = arr.index(maxi)
            j = i
            if i != 0 and i != len(arr)-1:
                while i < len(arr)-1:
                    if arr[i] > arr[i+1]:
                        dec+=1
                    i += 1
                while j > 0:
                    if arr[j] > arr[j-1]:
                        inc += 1
                    j -= 1
        
        if inc + dec == len(arr)-1:
            return not ismountain
                
            
            