class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1 2 2 3
        # 3 3 4 5
        #[3021,13025,18326,27390,28998]
        #29999
        people.sort()
        i=0
        j=len(people)-1
        boats = 0
        sums = 0
        print(people)
        while i <= j:
            if people[i] + people[j] > limit:
                #print(j ,people[i] + people[j])
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
                    