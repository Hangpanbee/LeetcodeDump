/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if (root == null) return null;
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        while (q.size() != 0) {
            root = q.poll();
            sb.append(root.val + ",");
            if (root.left != null) q.add(root.left);
            if (root.right != null) q.add(root.right);
            
        }
        //System.out.print(sb.toString() );
        return sb.toString();
        
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data == null) return null;
        String[] data_array = data.split(",");
        
        TreeNode ans = dfs(data_array, 0, -1, 10000);
        return ans;
    };
    
    public TreeNode dfs(String[] data, int index, int lower, int upper) {
        if (index >= data.length) {
            return null;
        };
        //System.out.println(data);
        TreeNode root = new TreeNode(Integer.parseInt(data[index]));
        root.left = null;
        root.right = null;
        
        for (int i = index + 1; i < data.length; i++) {
            int curr_int = Integer.parseInt(data[i]);
            if (lower < curr_int && curr_int < root.val) {
                root.left = dfs(data, i, lower, root.val);
                break;
            }; 
        };
        
        for (int i = index + 1; i < data.length; i++) {
            int curr_int = Integer.parseInt(data[i]);
            if (root.val < curr_int && curr_int < upper) {
                root.right = dfs(data, i, root.val, upper);
                break;
            };
        };
        
        return root;
        
        
        
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;