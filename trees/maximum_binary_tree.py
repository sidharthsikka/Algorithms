from node_class import Node

def constructMaximumBinaryTree(nums):
    size = len(nums)
    if(size != 0):
        max_index = max(nums)
        root = Node(nums[max_index])
        if (max_index > 0):
            leftarr = nums[0:max_index]
            root.left = constructMaximumBinaryTree(leftarr)
        else:
            root.left = None
        if (max_index < size-1):
            rightarr = nums[max_index+1:size]
            root.right = constructMaximumBinaryTree(rightarr)
        else:
            root.right = None
        return root
    return None

def max(nums):
    size = len(nums)
    max = nums[0]
    index = 0
    for i in range(0,size):
        if(nums[i] > max):
            index = i
            max = nums[i]
    return index
