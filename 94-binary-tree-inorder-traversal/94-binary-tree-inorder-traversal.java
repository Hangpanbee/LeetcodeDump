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
    public List<Integer> inorderTraversal(TreeNode root) {
        TreeNode curr = root;
        // curr = 1
        List<Integer> ans = new LinkedList<>();
        while (curr != null) {
            if (curr.left == null) {
                ans.add(curr.val);
                // ans = [1]
                curr = curr.right;
                // curr = 2
            } else {
                TreeNode prev = curr.left;
                // prev = 3
                while (prev.right != null && prev.right != curr) {
                    prev = prev.right;
                }
                
                if (prev.right == null) {
                    prev.right = curr;
                    // prev.right = 2
                    curr = curr.left;
                    // curr = 3
                } else {
                    prev.right = null;
                    ans.add(curr.val);
                    curr = curr.right;
                }
                
                
            }
        }
        
        return ans;
        
    }
}