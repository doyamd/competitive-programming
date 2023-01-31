class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i = 0
        j = 0
        players.sort()
        trainers.sort()
        match = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
            else:
                j += 1
        return match