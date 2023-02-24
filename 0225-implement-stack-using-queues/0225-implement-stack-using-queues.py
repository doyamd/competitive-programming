class MyStack:

    def __init__(self):
        self.stack = []        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) != 0:
            temp = self.stack[-1]
            del self.stack[-1]
            return temp
        else:
            return
    def top(self) -> int:
         if len(self.stack) != 0:
            temp = self.stack[-1]
            return temp
         else:
            return
    def empty(self) -> bool:
         if len(self.stack) != 0:
            return False
         else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()