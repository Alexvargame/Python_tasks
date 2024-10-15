import time
from threading import Thread
import threading

class CountdownTask:
    def __init__(self):
        self._running=True
    def terminate(self):
        self._running=False
    
    def run(self,n):
        while self._running and n>0:
            print('T-minus',n)
            n -= 1
            time.sleep(1)

##c=CountdownTask()
##t=Thread(target=c.run,args=(10,))
##t.start()
##c.terminate()
##print(t.join())

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()
    def run(self):
        # '''Запустить таймер и уведомлять ждущие потокипосле каждого интервал480   '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
    def wait_for_tick(self):
    #Ждать следующего срабатывания таймера

        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()
# Пример использования таймера
ptimer = PeriodicTimer(5)

ptimer.start()
# Два потока, синхронизирующихся по таймеру
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1
def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(3,)).start()        
            
              



if __name__ == '__main__':
    
    pass
