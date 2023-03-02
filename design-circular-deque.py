class MyCircularDeque:

    def __init__(self, k: int):
        self.lis = [0 for i in range(k)]
        self.size = k
        self.front = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
                self.rear = 0
            else:
                self.front = (self.front - 1) % self.size
            self.lis[self.front] = value
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.lis[self.rear] = value
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            
            if self.front == self.rear :
                self.front = None
                self.rear = None   
            else:
               self.front = (self.front+1) % self.size 
            return True
        else:
             return False
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            
            if self.front == self.rear :
                self.front = None
                self.rear = None
            else:
                self.rear = (self.rear-1) % self.size
            return True
        else:
            return False


    def getFront(self) -> int:
        if not self.isEmpty():
            return self.lis[self.front]
        return -1
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.lis[self.rear]
        return -1
    def isEmpty(self) -> bool:
        if self.front == None and self.rear == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if not self.isEmpty():
            if (self.front == 0 and self.rear == self.size-1) or (self.rear - self.front == -1): 
                return True
        else: 
            return False 
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()