class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for i in timePoints:
            h,m = map(int,i.split(':'))
            time.append(h*60+m)
        time.sort()
        ans = float('inf')

        for i in range(1,len(time)):
            ans = min(ans,time[i]-time[i-1])
        ans = min(ans,1440 - (time[-1]-time[0]))
        return ans
