from node_class import Node

def subtree_sum(root):
    result = {}
    def sum(node):
        if not node:
            return 0
        sum = node.val + sum(node.left) + sum(node.right)
        if sum in result:
            result[sum] = result[sum] + 1
        else:
            result[sum] = 1
        return sum
    sum(root)
    maximum = max(result.values())
    return [key for key,value in result.items() if value == maximum]