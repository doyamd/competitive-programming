class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j: 
            heig = min(height[i], height[j])
            width = j-i
            if heig*width >= max_area:
                max_area = heig*width
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:  
                i += 1
                j -= 1
        return max_area
            
