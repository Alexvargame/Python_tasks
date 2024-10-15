class TimeMap(object):

    def __init__(self):
        self.adict = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        print(self.adict)
        print('set', key, value, timestamp)
        if not self.adict.get(key):
            self.adict[key] = []
        self.adict[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res  = ''
        values = self.adict.get(key, [])
        l = 0
        r = len(values) - 1

        # if key in self.adict:
        print('get', self.adict, self.adict[key][-1])

        while l <= r:
            mid = (l + r) // 2
            if lst[mid][1] <= timestamp:
                res = lst[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    #print('res', carFleet(10, [6, 8], [3, 2]))
    pass



if __name__ == "__main__":
    main()
