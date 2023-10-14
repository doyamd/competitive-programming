class ListNode:
    def __init__(self,key=0, val=0):
        self.val,self.key = val,key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head,self.tail = ListNode(), ListNode()
        self.head.next,self.tail.prev = self.tail,self.head
    
    def remove(self,node):
        temp = node.prev
        temp.next = node.next
        temp = temp.next
        temp.prev = node.prev
        node.next = None
        node.prev = None
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.add(self.d[key])
            return self.d[key].val
        return -1
       
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = ListNode(key,value)
        self.add(self.d[key])
        if len(self.d) > self.cap:
            temp = self.head.next
            self.remove(temp)
            del(self.d[temp.key])
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)