class Node:
    
    def __init__(self, val=-1, next=None, level=None):
        self.val = val
        self.next = None
        self.down = None
        self.LLpointer = None
        self.LLnext = None
        self.LLprev = None
        
class Skiplist:

    def __init__(self):
        self.levels = []
        prev = None
        for i in range(20):
            node = Node(-9999999999)
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node
            
    def _iter(self, val):
        # collect all of the same val
        list_of_nodes = []
        curr = self.levels[0]
        while curr:
            while curr.next and curr.next.val < val:
                curr = curr.next
            list_of_nodes.append(curr)
            curr = curr.down
        return list_of_nodes
    
    def getMax(self):
        maxVal = self.search(9999999999999)
        return maxVal
    
    def search(self, target: int) -> bool:
        last_nodes = self._iter(target)[-1]
        #print(last_nodes, last_nodes.val)
        return last_nodes.val

    def add(self, LLnode) -> None:
        list_of_nodes = self._iter(LLnode.val)
        prev = None
        for i in range(len(list_of_nodes)-1,-1,-1):
            node=Node(LLnode.val)
            node.LLpointer = LLnode
            node.next, node.down = list_of_nodes[i].next, prev
            list_of_nodes[i].next = node
            prev=node
            rand=random.random()
            if rand>0.5:
                break
                
        
                
    def erase(self, num: int) -> bool:
        list_of_nodes = self._iter(num)
        delNode = None
        prev = None
        for i in range(len(list_of_nodes)):
            if list_of_nodes[i].next and list_of_nodes[i].next.val == num:
                delNode = list_of_nodes[i].next.LLpointer
                list_of_nodes[i].next = list_of_nodes[i].next.next
        
        return delNode


class DoubleLinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(0)
        self.head.LLnext = self.tail
        self.tail.LLprev = self.head
        
    def add(self, val):
        newNode = Node(val)
        newNode.LLnext = self.tail
        newNode.LLprev = self.tail.LLprev
        self.tail.LLprev.LLnext = newNode
        self.tail.LLprev = newNode
        return newNode
    
    def pop(self):
        return self.unlink(self.tail.LLprev).val
    
    def peek(self):
        #print(self.tail.LLprev.val)
        return self.tail.LLprev.val
    
    def unlink(self, node):
        #print("unlink", node.val, node.LLprev.val, node.LLnext.val)
        node.LLprev.LLnext = node.LLnext
        node.LLnext.LLprev = node.LLprev
        #print(self.tail.LLprev.val)
        return node
    
    def print_ll(self):
        root = self.head
        while root:
            #print('rrot', root.val)
            root = root.LLnext
        

class MaxStack:

    def __init__(self):
        self.skipList = Skiplist()
        self.LLstack = DoubleLinkedList()
        

    def push(self, x: int) -> None:
        newNode = self.LLstack.add(x)
        self.skipList.add(newNode)

    def pop(self) -> int:
        topVal = self.LLstack.pop()
        self.skipList.erase(topVal)
        #print(self.LLstack.tail.LLprev.val)
        return topVal

    def top(self) -> int:
        return self.LLstack.peek()

    def peekMax(self) -> int:
        return self.skipList.getMax()
        

    def popMax(self) -> int:
        maxVal = self.peekMax()   
        poppedNode = self.skipList.erase(maxVal)
        self.LLstack.unlink(poppedNode)
        return maxVal


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()