from node_class import Node

def left_most_node_each_level(root):
    result = []
    stack = [(root,1)]
    while len(stack) != 0:
        (temp, level) = stack.pop()
        if level > len(result):
            result.append(temp.val)
        if temp.right:
            stack.append((temp.right, level + 1))
        if temp.left:
            stack.append((temp.left, level + 1))
    return result

def main():
    print(left_most_node_each_level(Node.test_tree()))

main()