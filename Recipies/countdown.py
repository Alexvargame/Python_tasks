import time
import threading
import pickle

class Countdown:

    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)
    def __getstate__(self):
        return self.n
    def __setstate__(self, n):
        self.__init__(n)


c=Countdown(30)

f=open('cstate.p','wb')
pickle.dump(c,f)
f.close()
f=open('cstate.p','rb')
pickle.load(f)
