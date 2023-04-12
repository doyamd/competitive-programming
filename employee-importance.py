"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, emp: List['Employee'], id: int) -> int:
        d = defaultdict(list)
        for i in range(len(emp)):
            d[emp[i].id].append(emp[i].importance)
            d[emp[i].id].extend(emp[i].subordinates)
        
        sums = 0
        
        def importance(lis):
            nonlocal sums
            if len(lis) == 1:
                sums += lis[0]
                return 
            sums += lis[0]
            for i in lis[1:]:
                importance(d[i])
        importance(d[id])

        return sums