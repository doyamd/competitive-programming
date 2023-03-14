class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        j = len(citations)-1
        length = len(citations)
        while i <= j:
            mid = (i+j)//2
            if length - mid > citations[mid] :
                i = mid + 1
            else:
                j = mid - 1
        
        return length - j - 1