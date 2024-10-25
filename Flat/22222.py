import pickle

class MyClass():
    def __init__(self):
        self.info = OtherClass(option=1)

    def pickle(self):
        f = file('11', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    def unpickle(self):
        f = file('11', 'rb')
        pickle.load(f)
        f.close()


class OtherClass():
    def __init__(self, option):
        self.property = option * 2


mydata = MyClass(option=5)

mydata.pickle()
