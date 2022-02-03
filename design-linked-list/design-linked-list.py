class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #self.printAll()
        #print('end', index, self.size)
        if index >= self.size or index < 0: return -1
        
        if index == 0: return self.head.val
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        if not self.head: 
            self.head = newNode
        else:
            curr = self.head
            self.head = newNode
            newNode.next = curr
            curr.prev = newNode
        self.size += 1
            

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
    

        if self.size == 0: 
            self.addAtHead(val)
            

        else: 
            curr = self.head
            for i in range(self.size - 1):
                curr = curr.next
        
            curr.next = newNode
            newNode.prev = curr
            self.size += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size or index < 0: return
        
        if index == 0: self.addAtHead(val)
        elif index == self.size: self.addAtTail(val)
        else:
            addedNode = Node(val)
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            
            addedNode.next = curr.next
            addedNode.next.prev = addedNode
            curr.next = addedNode
            addedNode.prev = curr
            
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size or index < 0: return
        
        curr = self.head
        if index == 0: self.head = curr.next
        elif index == self.size: 
            while curr.next:
                curr = curr.next
            curr.next = None
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        
        self.size -= 1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)