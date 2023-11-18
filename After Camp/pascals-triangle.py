class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]
        numRows -= 2

        for i in range(numRows):
            i = 0
            j = 1
            arr = [1]
            while j in range(len(ans[-1])):
                arr.append(ans[-1][i] + ans[-1][j])
                i += 1
                j += 1
            arr.append(1)
            ans.append(arr)
        return ans

        