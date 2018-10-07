from node_class import Node

def merge_two_binary_tress(t1,t2):
    node = None
    if t1 and t2:
        node = Node(t1.val + t2.val)
        node.left = merge_two_binary_tress(t1.left,t2.left)
        node.right = merge_two_binary_tress(t1.right,t2.right)
    elif t1:
        node = Node(t1.val)
        node.left = merge_two_binary_tress(t1.left, None)
        node.right = merge_two_binary_tress(t1.right, None)
    elif t2:
        node = Node(t2.val)
        node.left = merge_two_binary_tress(t2.left, None)
        node.right = merge_two_binary_tress(t2.right, None)
    return node