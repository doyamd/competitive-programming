def flip(arr,ind):
    k=0
    j=ind
    while k < ind/2 and j > ind/2:
        arr[k], arr[j] = arr[j], arr[k]
        k += 1
        j -= 1
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans =[]
        indx= len(arr)-1
        for i in range(indx,-1,-1):
            maxi = max(arr[0:i+1])
            ind = arr.index(maxi)
            #print( maxi , ind+1)
            ans.append(ind+1)
            flip(arr,ind)
            ans.append(i+1)
            flip(arr,i)
            
        return ans