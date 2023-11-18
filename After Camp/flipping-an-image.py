class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # ans = [0 for _ in range(len(image))[0 for _ in range(len(image))]]
        for i in range(len(image)):
            image[i] = image[i][::-1]
        
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image