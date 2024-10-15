##
##def frange(start,stop,increment):
##    x=start
##    while x<stop:
##        yield x
##        x+=increment
##
##for n in frange(0,4,0.5):
##    print(n)
##
##def countdown(n):
##    print('Starting to count from',n)
##    while n>0:
##        yield n
##        n-=1
##    print('Done')
##
##c=countdown(3)
##print(c)
##next(c)
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
        
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
        
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
