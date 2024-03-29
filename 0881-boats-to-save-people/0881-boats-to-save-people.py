class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        boats = 0
        while i <= j:
            if people[i] + people[j] > limit:
                boats += 1
                j -= 1
            elif  people[i] + people[j] < limit:
                boats +=1
                i +=1
                j -=1 
                
            elif people[i] + people[j]  == limit:
                boats += 1
                i += 1
                j -= 1
            if i == j:
                boats += 1
                i += 1
                j -= 1
                
        return boats
                    