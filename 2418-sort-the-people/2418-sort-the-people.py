class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            mini=heights[i]
            indx=i
            for j in range(i+1,len(heights)):
                if mini<heights[j]:
                    indx=j
                    mini=heights[j]
            if indx != i:
                heights[i],heights[indx]=heights[indx],heights[i]
                names[i],names[indx]=names[indx],names[i]
        return names