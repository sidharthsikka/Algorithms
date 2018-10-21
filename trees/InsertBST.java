/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class InsertBST {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root != null){
            if(val >= root.val){
                root.right = insertIntoBST(root.right, val);
            } else{
                root.left = insertIntoBST(root.left, val);
            }
            return root;
        }
        TreeNode insert = new TreeNode(val);
        return insert;
    }
}