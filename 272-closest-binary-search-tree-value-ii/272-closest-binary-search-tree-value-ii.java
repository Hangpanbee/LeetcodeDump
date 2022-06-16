/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        
        TreeNode curr = root;
        // keep a minHeap to evict old key
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(k, new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
                return ((Double)Math.abs(i2-target)).compareTo((Double)Math.abs(i1-target));
            }
        });
        while (curr != null) {
            // curr = 4
            // curr = 2
            // curr = 1
            // curr = 2
            // curr = 3
            //System.out.println(curr.val);
            if (curr.left == null) {
                if (minHeap.size() < k) minHeap.add(curr.val);
                // minHeap = [2,3]
                else {
                    if (Math.abs(minHeap.peek()-target) > Math.abs(curr.val-target)) {
                        minHeap.poll();
                        minHeap.add(curr.val);
                    }
                }
                curr = curr.right;
                // curr = 2
            } else {
                TreeNode prev = curr.left;
                // prev = 2
                // prev = 1
                // prev = 1
                while (prev.right != null && prev.right != curr) {
                    prev = prev.right;
                }
                // prev = 3
                // prev = 1
                if (prev.right == null) {
                    prev.right = curr;
                    // prev.right = 4 -> 3.right = 4
                    // prev.right = 1 -> 1.right = 2
                    curr = curr.left;
                    // curr = 2
                    // curr = 1
                } else {
                    //restore the changes
                    if (minHeap.size() < k) minHeap.add(curr.val);
                    else {
                        if (Math.abs(minHeap.peek()-target) > Math.abs(curr.val-target)) {
                            minHeap.poll();
                            minHeap.add(curr.val);
                            //minHeap = [1, 2]
                        }
                    }
                    prev.right = null;
                    curr = curr.right;
                }
                
            }
            
        }
        List<Integer> ans = new ArrayList<>(minHeap);
        
        return ans;
        
        
        
    }
}