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
class BSTIterator {
    Stack<TreeNode> stack;
    
    public BSTIterator(TreeNode node) {
        stack = new Stack<>();
        TreeNode root = node;
        updateStack(root);
    }
    
    public int next() {
        TreeNode currNode = stack.pop();
        updateStack(currNode.right);
        return currNode.val;
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
    }
    
    private void updateStack(TreeNode root) {
        while (root != null) {
            stack.add(root);
            root = root.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */