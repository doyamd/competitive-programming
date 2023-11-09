class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners=collections.defaultdict(int)
        losers=collections.defaultdict(int)
        win=[]
        lose=[]
        ans=[]
        for i in range(len(matches)):
            winners[matches[i][0]]+=1
        for i in range(len(matches)):
            losers[matches[i][1]]+=1   
        for player,no in losers.items():
            if no==1:
                lose.append(player)
        for player, no in winners.items():
            if player not in losers:
                win.append(player)
        win.sort()
        lose.sort()
        return [win,lose]


        