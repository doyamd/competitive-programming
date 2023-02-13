class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def get(self, index: int) -> int:
        link = self.head
        i = 0
        while i < index and link.next:
                link = link.next
                i += 1
        if index < self.count and index >= 0 and self.head:
            return link.val
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:
        new_node = node(val)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        #print(self.head.val)
        self.count += 1
    def addAtTail(self, val: int) -> None:
        new_node = node(val)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        #print(self.tail.val)
        self.count += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = node(val)
        link = self.head
       
        i = 0
        while i < index -1 and link.next:
                link = link.next
                i += 1
        if index <= self.count and index >=0:
            if index == 0:
                self.addAtHead(val)
            else :
                new_node.next = link.next
                link.next = new_node
                if self.tail.next:
                    self.tail = self.tail.next
            
            
            self.count += 1
        
    def deleteAtIndex(self, index: int) -> None:
        link = self.head
        i = 0
        while i < index -1 and link.next:
                link = link.next
                i += 1
        if index < self.count and index >=0:
            if index == 0:
                self.head = self.head.next
            else:
                if link and link.next:
                    link.next = link.next.next
                if link.next == None:
                    self.tail = link
            if self.count == 0:
                self.head = self.tail = None

            self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)