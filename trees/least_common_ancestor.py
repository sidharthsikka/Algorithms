from node_class import Node

def least_common_ancestor(root,p,q):
    if not root:
        return None
    if root is p or root is q:
        return root
    left = least_common_ancestor(root.left,p,q)
    right = least_common_ancestor(root.right,p,q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
