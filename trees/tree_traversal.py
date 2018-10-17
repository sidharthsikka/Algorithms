from node_class import Node

def inorder_recursive(root):
    result = []
    def rec(node):
        if node:
            rec(node.left)
            result.append(node.val)
            rec(node.right)
    rec(root)
    return result

def postorder_recursive(root):
    result = []
    def rec(node):
        if node:
            rec(node.left)
            rec(node.right)
            result.append(node.val)
    rec(root)
    return result

def preorder_recursive(root):
    result = []
    def rec(node):
        if node:
            result.append(node.val)
            rec(node.left)
            rec(node.right)
    rec(root)
    return result

def inorder_iterative(root):
    if not root:
        return []
    result = []
    stack = []
    stack.append(root)
    backup = False

    while stack:
        print([str(node.val) for node in stack])   
        head = stack[-1]
        if head.left and not backup:
            stack.append(head.left)
        elif head:
            backup = True
            temp = stack.pop()
            result.append(temp.val)
            if temp.right:
                stack.append(temp.right)
                backup = False
        elif head.right:
            stack.append(head.right)

    return result

def main():
    root = Node.test_tree()
    print(inorder_iterative(root))
    

main()
