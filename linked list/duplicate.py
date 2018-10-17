from node_class import Node

def duplicate(head):
    if head is None:
        return None
    result = Node(head.val)
    temp = head.next
    temp1 = result
    old_to_new = {}
    old_to_new[head] = result
    while temp:
        x = Node(temp.val)
        old_to_new[temp] = x
        temp1.next = x
        temp1 = x
        temp = temp.next
    temp = head
    while temp:
        if temp.random:
            old_to_new[temp].random = old_to_new[temp.random]
        temp = temp.next
    return result

def duplicate_1(head):
    dic = dict()
    dic[None] = None
    p = head
        
    while p:
        dic[p] = Node(p.val)
        p = p.next
        
    p = head
    while p:
        dic[p].next = dic[p.next]
        dic[p].random = dic[p.random]
        p = p.next
            
    return dic[head]