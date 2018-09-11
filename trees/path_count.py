# On leetcode it is called path_sum
from node_class import Node

def path_count(root, count, target):
    if root.is_leaf():
        if root.val + count == target:
            return True
        return False
    return path_count(root.left, count+root.val, target) or path_count(root.right, count+root.val, target)

def main(root, target):
    path_count(root, 0, target)