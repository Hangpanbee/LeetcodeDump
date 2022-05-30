class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, key, value) -> Node:
        prevTail = self.tail.prev
        newNode = Node(key, value)
        prevTail.next = newNode
        newNode.prev = prevTail
        newNode.next = self.tail
        self.tail.prev = newNode
        return newNode
        
    def removeHead(self) -> int:
        val = self.head.next.key
        temp = self.head.next.next
        self.head.next = temp
        temp.prev = self.head
        return val
        
    def remove(self, node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
        

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = LinkedList()
        self.mapKeyToNode = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.mapKeyToNode: return -1
        node = self.mapKeyToNode[key]
        nodeVal = node.val
        self.dll.remove(node)
        newNode = self.dll.add(key, nodeVal)
        self.mapKeyToNode[key] = newNode
        return nodeVal

    def put(self, key: int, value: int) -> None:
        if key in self.mapKeyToNode:
            node = self.mapKeyToNode[key]
            self.dll.remove(node)
            newNode = self.dll.add(key, value)
            self.mapKeyToNode[key] = newNode
        else:
            if len(self.mapKeyToNode) + 1 > self.capacity:
                headVal = self.dll.removeHead()
                del self.mapKeyToNode[headVal]
            newNode = self.dll.add(key, value)
            self.mapKeyToNode[key] = newNode
         

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)