from node_class import Node

# sorted arr
def build_tree(arr):
    if arr is None:
        return None
    elif len(arr) == 1:
        temp = Node(arr[0])
        return temp
    else:
        mid = len(arr)//2
        left_child = build_tree(arr[0:mid])
        right_child = build_tree(arr[mid+1:])
        node = Node(arr[mid], left_child, right_child)
        return node

def build_tree_2(inorder, postorder):
    if not inorder:
        return
    if len(inorder) == 1:
        return Node(inorder[0])
    root_val = postorder[-1]
    left_tree = inorder[:inorder.index(root_val)]
    left_node = build_tree_2(left_tree, postorder[:len(left_tree)])
    right_node = build_tree_2(inorder[len(left_tree)+1:], postorder[len(left_tree):-1])
    root_node = Node(root_val,left_node,right_node)
    return root_node

