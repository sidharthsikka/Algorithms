/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BinaryTreePruning {
    public TreeNode pruneTree(TreeNode root) {
        if(root != null){
            TreeNode left = pruneTree(root.left);
            TreeNode right = pruneTree(root.right);
            if(root.val == 1 || left != null || right != null){
                root.left = left;
                root.right = right;
                return root;
            }
            return null;
        }
        return null;
    }
}