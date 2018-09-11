from node_class import Node
from collections import deque

def level_order(root):
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        temp = queue.popleft()
        result.append(temp.val)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    return result

def main():
    root = Node.test_tree()
    print(level_order(root))

main()
