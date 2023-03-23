class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def choice(nums,i,j,turn):
            if i >= j:
                return nums[j]
            if turn :
                return max((nums[i] + choice(nums,i+1,j,not turn)), (nums[j] + choice(nums,i,j - 1,not turn )))
            else:
                return min((choice(nums,i+1,j,not turn)), (choice(nums,i,j -1,not turn)))

        player1 = 0
        player2 = 0
        turn = True
        for i in range(len(nums)):
            player2 += nums[i]

        player1 += choice(nums,0,len(nums)-1, turn)
        
        player2 -= player1
        
        return (player1 >= player2)