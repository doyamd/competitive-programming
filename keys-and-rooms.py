class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = defaultdict(list)
        for i in range(len(rooms)):
            for j in rooms[i]:
                d[i].append(j)
        visited = set()
        queue = deque([0])
        visited.add(0)
        while queue:
            length = len(queue)
            node = queue.popleft()
            if len(visited) == len(rooms):
                return True
            for i in d[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False