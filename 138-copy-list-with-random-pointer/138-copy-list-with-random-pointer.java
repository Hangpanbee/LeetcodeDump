/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        HashMap<Node, Node> map = new HashMap<>();
        Node start = head;
        while (start != null) {
            Node copyNode = new Node(start.val);
            map.put(start, copyNode);
            start = start.next;
        };
        
        start = head;
        while (start != null) {
            map.get(start).next = map.get(start.next);
            map.get(start).random = map.get(start.random);    
            
            start = start.next;
        };
        
        return map.get(head);
        
    }
}