/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q111MinimumTreeDepth {
    Double minDepth = Double.POSITIVE_INFINITY;
    
    public void traverse(TreeNode node, int depth) {
        if(node == null) {
            return;
        }
        
        if(node.left == null && node.right == null) {
            minDepth = Math.min(minDepth, (double) depth);
        }
        
        traverse(node.left, depth + 1);
        traverse(node.right, depth + 1);
    }
    
    public int minDepth(TreeNode root) {
        if(root == null) {
            return 0;
        }
        
        traverse(root, 1);
        return minDepth.intValue();
    }
}
