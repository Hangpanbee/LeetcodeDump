class Node:
    
    def __init__(self, val=-1, next=None, level=None):
        self.val = val
        self.next = None
        self.down = None
        self.LLnext = None
        self.LLprev = None


class Skiplist:

    def __init__(self):
        self.levels = []
        prev = None
        for i in range(16):
            node = Node(-9999999999, 16)
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
    
    
    def search(self, target: int) -> bool:
        last_nodes = self._iter(target)[-1]
        return last_nodes.next and last_nodes.next.val == target

    def add(self, num: int) -> None:
        list_of_nodes = self._iter(num)
        prev = None
        for i in range(len(list_of_nodes)-1,-1,-1):
            node=Node(num)
            node.next, node.down = list_of_nodes[i].next, prev
            list_of_nodes[i].next = node
            prev=node
            rand=random.random()
            if rand>0.5:
                break
        
                
    def erase(self, num: int) -> bool:
        list_of_nodes = self._iter(num)
        delNode = False
        prev = None
        for i in range(len(list_of_nodes)):
            if list_of_nodes[i].next and list_of_nodes[i].next.val == num:
                delNode = True
                list_of_nodes[i].next = list_of_nodes[i].next.next
        
        return delNode


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)