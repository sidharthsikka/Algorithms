class Node:
    def __init__(self, val, next=None, random=None):
        self.next = next
        self.val = val
        self.random = random

    @staticmethod
    def test_list():
        v = Node(6)
        c = Node(5, v)
        z = Node(4, c)
        y = Node(3, z)
        x = Node(2, y)
        head = Node(1, x)
        return head

    @staticmethod
    def test_list_1():
        a = Node(1)
        b = Node(2,a)
        c = Node(3,b)
        return c

    @staticmethod
    def print_list(z):
        while z:
            print(z.val)
            z = z.next
    
    @staticmethod
    def test_random_list():
        x = Node(1)
        y = Node(2,x)
        c = Node(3,y)
        z = Node(4,c,y)
        v = Node(5,z)
        c.random = v
        return v