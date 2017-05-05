class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    #string representation
    def __str__(self):
        if self.next is None:
            return "Node({}) > /".format(self.elem)
        else:
            return "Node({0}) > Node({1})".format(self.elem, self.next.elem)
    
    #for equality operator
    def __eq__(self, other):   
        return self.elem == other

    # (string) is intended to produce output that is mostly machine-readable
    def __repr__(self):   
        return str(self.elem)   #is this right?
