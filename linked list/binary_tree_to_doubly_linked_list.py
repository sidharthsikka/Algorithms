from collections import deque
from trees.node_class import Node
from node_class import Node

# Doubly Linked List is circular(not tested)
def binary_tree_to_doubly_linked_list(root, type):
    if root:
        left = binary_tree_to_doubly_linked_list(root.left, "left")
        right = binary_tree_to_doubly_linked_list(root.right, "right")
        left.prev = right
        root.prev = left
        right.prev = root
        right.next = left
        left.next = root
        root.next = right
        if type == "left":
            return left.next
        return left
    return root

# Modifies root in place so dont need to return anything
def flatten(root):
    queue = deque()
    def pre_order(root):
        if root:
            queue.append(root)
            pre_order(root.left)
            pre_order(root.right)
    pre_order(root)
    prev = None
    while(len(queue) != 0):
        head = queue.popleft()
        head.left = None
        head.right = None
        if prev != None:
            prev.right = head
        prev = head