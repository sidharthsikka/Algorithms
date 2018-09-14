from node_class import Node

class Cache:
    def __init__(self):
        self.sim = None
        self.length = 0
        self.item_cache = {}
        self.head = self.sim
        self.end = self.sim

    def put(self,key,value):
        if self.item_cache[key]:
            temp = self.item_cache[key]
            prev = temp.prev
            nex = temp.next
            prev.next = nex
            nex.prev = prev
            self.end.next = temp
            temp.prev = self.end
            self.end = temp
        else:
            if self.length > 8: # assuming the cache can hold 8 items
                self.head.next.prev = None
                self.head = self.head.next
            temp = Node(value,previous=self.end)
            self.item_cache[key] = temp
            if self.end:
                self.end.next = temp
            self.end = temp
            self.length+=1
            if self.head is None:
                self.head = temp
    
    def get(self,key):
        if self.item_cache[key]:
            temp = self.item_cache[key]
            prev = temp.previous
            nex = temp.next
            prev.next = nex
            nex.previous = prev
            self.end.next = temp
            temp.prev = self.end
            self.end = temp
        return -1