class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxib=-1
        maxia=-1
        for i in range(len(arr)-1,-1,-1):
            
            maxia = max(maxia,arr[i])
            arr[i] = maxib
            maxib = maxia
            
        return arr
      
            
            
                