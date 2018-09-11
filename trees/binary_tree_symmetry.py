from node_class import Node

def symmetry(node1, node2):
    if node1 and node2:
        if node1. val == node2.val:
            return symmetry(node1.left,node2.right) and symmetry(node1.right,node2.left)
        return False
    elif node1 is None and node2 is None:
        return True
    return False

def main(root):
    if root is None:
        return True
    symmetry(root.left, root.right)    

