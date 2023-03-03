# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        i = 1
        j = n
        while i <= j:
            mid =( i + j)//2
            if not isBadVersion(mid):
                i = mid + 1
            elif isBadVersion(mid):
                j = mid - 1
        return i