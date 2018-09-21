# On leetcode it is called path_sum
from node_class import Node

def path_count(root, count, target):
    if root.is_leaf():
        if root.val + count == target:
            return True
        return False
    return path_count(root.left, count+root.val, target) or path_count(root.right, count+root.val, target)

def path_sum_three(root,sum):
    allSums = dict()
    sums = dict() # value to frequency
    def DFS(root, sums):
        if root:
            temp = dict()
            for key, value in sums.items():
                temp[key + root.val] = temp.get(key + root.val,0) + value
            temp[root.val] = temp.get(root.val, 0) + 1
            for key, value in temp.items():
                allSums[key] = allSums.get(key,0) + value
            DFS(root.left,temp)
            DFS(root.right,temp)
    DFS(root,sums)
    if sum in allSums:
        return allSums[sum]
    return 0

def main(root, target):
    path_count(root, 0, target)