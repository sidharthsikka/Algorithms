class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def __str__(self):
        return str(self.val)

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    @staticmethod
    def test_tree():
        one = Node(1)
        four = Node(4)
        child_three = Node(3,one,four)
        six = Node(6)
        eight = Node(8)
        child_seven = Node(7, six, eight)
        root = Node(5,child_three,child_seven)
        return root