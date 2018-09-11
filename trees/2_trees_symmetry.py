from node_class import Node

def symmetry(root1, root2):
    if root1 and root2 and root1.val == root2.val:
        return symmetry(root1.left, root2.left) and symmetry(root1.right, root2.right)
    elif root1 is None and root2 is None:
        return True
    return False