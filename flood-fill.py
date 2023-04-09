class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        main = image[sr][sc]
        def change(i,j):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) :
                return 
            if image[i][j] != main or image[i][j] == color:
                return
            image[i][j] = color
            change(i-1, j)
            change(i+1, j)
            change(i, j-1)
            change(i, j+1)
        
        change(sr,sc)

        return image