class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []
        end = []
        d = {}
        ans = [-1 for _ in range(len(intervals))]

        for i in range(len(intervals)):
            start.append(intervals[i][0])
            d[intervals[i][0]] = i

        start.sort()
        
        for i in range(len(intervals)):
            insr = bisect_left(start, intervals[i][1])
            print(insr)
            if insr == len(intervals):
                continue
            ans[i] = d[start[insr]]

        return ans