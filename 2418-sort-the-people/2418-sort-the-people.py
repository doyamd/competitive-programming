class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #Insertion Sorting
        for i in range(1,len(heights)):
            key_height = heights[i]
            key_names = names[i]
            j = i-1
            while key_height > heights[j] and j>=0:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = key_height
            names[j+1] = key_names
            
        return names
                