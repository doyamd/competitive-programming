class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(bool)
        for i,j in edges:
            d[j] = True
        ans = []
        visited = set()
        for i, j in edges:
            visited.add(i)
            visited.add(j)
        visited = list(visited)
        for i in visited:
            if not d[i]:
                ans.append(i)

        return ans