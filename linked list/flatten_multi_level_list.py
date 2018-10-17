"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []            
        temp = head
        prev = None
        result = None
        while len(stack) > 0 or temp != None:
            if temp:
                print(temp.val)
                x = Node(temp.val,None,None,None)
                x.prev = prev
                if temp.child:
                    stack.append(temp.next)
                    temp = temp.child
                elif temp.next:
                    temp = temp.next
                else:
                    if len(stack) > 0:
                        temp = stack.pop()
                    else:
                        temp = None
                if prev:
                    prev.next = x
                else:
                    result = x
                prev = x
            else:
                print("None")
                if prev:
                    prev.next = None
                if len(stack) > 0:
                    temp = stack.pop()
                else:
                    temp = None
        return result        