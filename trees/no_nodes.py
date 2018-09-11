from node_class import Node

def no_of_nodes(root):
    if root:
        return 1 + no_of_nodes(root.left) + no_of_nodes(root.right)
    return 0