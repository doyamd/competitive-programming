class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        heap = []
        for i in range(1,len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if len(heap) < ladders:
                    heappush(heap,diff)
                else:
                    prev_diff = diff
                    if heap and heap[0] < diff:
                        prev_diff = heappop(heap)
                        heappush(heap,diff)
                    if (bricks-prev_diff) >= 0:
                        bricks -= prev_diff
                    else:
                        return i-1
        return i