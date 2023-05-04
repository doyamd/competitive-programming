class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = Counter(words)
        arr = []
        for key, v in d.items():
            arr.append(v)
        
        heapify(arr)
        
        largest = (nlargest(k,arr))
        ans = []
        visited = set()
        for i in largest:
            temp = []
            for key in words:
                if d[key] == i and key not in visited :
                    visited.add(key)
                    temp.append(key)
            temp.sort()
            for x in temp:
                if len(ans) < k:
                    ans.append(x)
        
        return ans