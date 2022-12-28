#
class Solution:
    def average(self, salary: List[int]) -> float:
        
       
        total=sum(salary)
        min_=min(salary)
        max_=max(salary)
     
        return (total-min_-max_)/(len(salary)-2)
