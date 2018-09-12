from node_class import Node

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
def add_two_numbers(head1, head2):
    result = None
    end = result
    carry = 0
    while head1 or head2:
        sum = 0
        if head1:
            sum+=head1.val
            head1 = head1.next
        if head2:
            sum+=head2.val
            head2 = head2.next
        sum+=carry
        carry = 0
        if sum>=10:
            carry = 1
            sum-=10
        temp = Node(sum)
        if end is None:
            result = temp
        else:
            end.next = temp
        end = temp
    if carry == 1:
        end.next = Node(1)
    return result

'''
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''
def add_two_numbers_2(head1,head2):
    if head1.val == 0:
        return head2
    if head2.val == 0:
        return head1
    def stack_sum(h1,h2):
        stack1 = list()
        stack2 = list()
        while h1:
            stack1.append(h1.val)
            h1 = h1.next
        while h2:
            stack2.append(h2.val)
            h2 = h2.next
        prev = None
        carry = 0
        while stack1 or stack2:
            sum = 0
            if len(stack1)>0:
                sum+=stack1.pop()
            if len(stack2)>0:
                sum+=stack2.pop()
            sum+=carry
            carry = 0
            if sum>=10:
                sum-=10
                carry = 1
            temp = Node(sum, prev)
            prev = temp
        if carry == 1:
            temp = Node(1, prev)
            prev = temp
        return prev
    result = stack_sum(head1, head2)
    return result

def main():
    l1 = Node.test_list()
    l2 = Node.test_list_1()
    Node.print_list(l1)
    Node.print_list(l2)
    l = add_two_numbers_2(l1,l2)
    Node.print_list(l)

main()