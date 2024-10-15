class TreeStore:

    def __init__(self,data):
        self.data=dict(zip([d['id'] for d in data],data))

    def getAll(self):
        return list(self.data.values())

    def getitem(self,id):
        return self.data[id]

    def getChildren(self,id):
        return [d for d in self.data.values() if d['parent']==id]
    
    def getParents(self,id):
        parents=[]
        count=id
        while count>1:
            it=self.data[count]
            parents.append(it)
            count=it['parent']
        if count==1:
            parents.append(self.data[1])
        return parents[1:]


   

def main():
    
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)
    print(ts.getAll())
    print(ts.getitem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getParents(7))
    



if __name__ == "__main__":
    main()

