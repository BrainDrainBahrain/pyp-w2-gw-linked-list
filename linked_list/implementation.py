from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
            
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return str([resnode for resnode in self])

    def __len__(self):
        return self.count()

    def __iter__(self):
        
        cur_node = self.start
        while cur_node is not None:
            yield cur_node.elem
            cur_node = cur_node.next
            
        raise StopIteration

    def __getitem__(self, index): # self[index]
        for idx, curr_node in enumerate(self):
            if idx == index:
                return curr_node
        raise IndexError
       

    def __add__(self, other):
        reslist = LinkedList()
        for elem in self:
            reslist.append(elem)
        for elem in other:
            reslist.append(elem)
        return reslist

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self
        

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
            
        for elem in zip(self, other):
            if elem[0] != elem[1]:
                return False
                
        return True
            
        '''[1, 2, 3, 4]
        [1, 3, 2, 4]
        [1, 2, 4, 5, 6]
        same length, same values, same order
        make sure same length
        iterate through make sure values are same
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = zip(a, b)
        c == [(1, 4), (2, 5), (3, 6)]'''

    def append(self, elem):
        newnode = Node(elem)
        
        if self.start == None:
            self.start = newnode
            self.end = newnode
        else:
            self.end.next = newnode
            self.end = newnode
        
        
        #[start][end] << [new_end]
        #[end]next = [new_end]
        

    def count(self):
        size = 0
        for curr_node in self:
            size += 1
        
        return size

    def pop(self, index=None):
        if self.start is None:
            raise IndexError
        prevnode = None
        idx = 0
        cur_node = self.start
        #last element set index value if none supplied
        if index is None:
            index = self.count() - 1
        #first element
        if index == 0:
            resnode = self.start
            self.start = self.start.next 
            return resnode.elem
        
        #iterate through 
        while cur_node is not None:
            if idx == index:
                prevnode.next = cur_node.next
                #last element
                if prevnode.next is None:
                    self.end = prevnode
                return cur_node.elem
            if cur_node.next is not None:
                prevnode = cur_node
            cur_node = cur_node.next
            idx += 1
        raise IndexError