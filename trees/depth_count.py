from node_class import Node

def depth_count(root, count):
    if root:
        return max(depth_count(root.left, count+1), depth_count(root.right, count+1))
    return count