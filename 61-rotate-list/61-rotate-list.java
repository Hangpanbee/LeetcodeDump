/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head==null || head.next == null) return head;
        
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;
        int length=0;
        while (fast.next != null) {
            fast = fast.next;
            length += 1;
        };
        
        for(int j=length-k%length; j > 0; j--) {
            slow = slow.next;
        };
        
    fast.next=dummy.next; //Do the rotation
    dummy.next=slow.next;
    slow.next=null;
    
    return dummy.next;
        
        
    };
}