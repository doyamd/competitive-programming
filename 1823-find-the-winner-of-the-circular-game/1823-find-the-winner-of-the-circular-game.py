class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count=0
        i=0
        start=0
        nums=list(range(1,n+1))
        while len(nums)>1:
            start=(start+k-1)%n
            nums.pop(start)
            n-=1
            
            
            
        return nums[0]
            
        