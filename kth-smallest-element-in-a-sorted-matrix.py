class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 1:
            return matrix[0][k-1]
        heap = []
        for i in range(len(matrix)):
            heappush(heap,(matrix[i][0],i,0))
        while heap:
            num, i,j = heappop(heap)
            k -= 1
            if not k:
                return num
            if (j + 1) < len(matrix):
                heappush(heap,(matrix[i][j+1],i,j+1))