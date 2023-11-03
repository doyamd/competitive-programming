class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        count = []
        for k, v in c.items():
            count.append(v)
        c2 = Counter(count)
        
        for i in count:
            if c2[i] != 1:
                return False
        return True