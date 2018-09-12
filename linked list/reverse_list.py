from node_class import Node

# Creates new reversed List
def reverse(head):
    y = Node(head.val)
    head = head.next
    x = y
    while head:
        temp = Node(head.val,x)
        head = head.next
        x = temp
    return x

# Iterative approach
def reverse_in_place(head):
    prev = None
    while head:
        nex = head.next
        head.next = prev
        prev = head
        head = nex
    return prev

# Recursive approach
def reverse_in_place_recurse(head, prev):
    if head is None:
        return prev
    temp = head.next
    head.next = prev
    result = reverse_in_place_recurse(temp, head)
    return result
        
def main():
    l = Node.test_list()
    y = reverse_in_place_recurse(l, None)
    Node.print_list(y)

main()