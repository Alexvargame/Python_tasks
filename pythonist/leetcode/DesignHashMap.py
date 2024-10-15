class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap(object):

    def __init__(self):
        self.max_entries = 1000
        self.entries = [ListNode() for _ in range(self.max_entries)]

    def hash(self, val):
        return val % self.max_entries

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.entries[self.hash(key)]

        while node and node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = ListNode(key=key, value=value)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.entries[self.hash(key)].next
        while node:
            if node.key == key:
                return node.value
            node = node.next
        else:
            return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        node = self.entries[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', carFleet(10, [6, 8], [3, 2]))
    pass



if __name__ == "__main__":
    main()
