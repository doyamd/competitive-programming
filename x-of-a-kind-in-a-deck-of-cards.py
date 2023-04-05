class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        count = Counter(deck)
        arr = list(count.values())
        if len(arr) == 1:
            return True
        gcd = math.gcd(arr[0],arr[1])
        for i in range(2,len(arr)):
            for j in range(i,len(arr)):
                gcd = math.gcd(gcd,arr[i])
        if gcd == 1:
            return False
        else:
            return True
        
            
                    




        
                 
                
# 1 1 2 2 2 2