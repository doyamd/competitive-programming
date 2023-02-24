class MinStack:

    def __init__(self):
        self.stack = []        
        self.mini_s = []
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mini_s : 
            self.mini_s.append(x)
        else:
            if x <= self.mini_s[-1]:
                self.mini_s.append(x)
    def pop(self) -> None:
        temp = self.stack.pop()
        if self.mini_s:    
            if self.mini_s[-1] == temp:
                self.mini_s.pop()
            return temp
        else:
            return
    def top(self) -> int:
         if len(self.stack) != 0:
            return self.stack[-1]
         else:
            return
    def getMin(self) -> int:
        if len(self.mini_s) != 0:
            return self.mini_s[-1]
        else:
            return
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()