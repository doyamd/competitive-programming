#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        box_operation=[]
        for i in range(len(boxes)):
            j=0
            count=0
            while j<len(boxes):
                if boxes[j]=='1':
                    count+=abs(j-i)
                j+=1
            box_operation.append(count)
        return box_operation
