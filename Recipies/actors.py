from queue import Queue
from threading import Thread, Event

# Страж, использующийся для отключения
class ActorExit(Exception):
    pass

class Actor:

    def __init__(self):
        self._mailbox = Queue()
    def send(self, msg):

    #Посылает сообщение в актор

        self._mailbox.put(msg)
    def recv(self):

     #Получает входящее сообщение

        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg
    def close(self):
        #
     #Закрывает актор и отключает его

        self.send(ActorExit)
    def start(self):

     #Запускает конкурентное выполнение

        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()
    def _bootstrap(self):
        try:

            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()
    def join(self):
        self._terminated.wait()
    def run(self):

     #Запускает метод, который реализует пользователь

     while True:
         msg = self.recv()
# Пример ActorTask
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got:', msg)



p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()

from threading import Event
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None
    def set_result(self, value):
        self._result = value
        self._evt.set()
    def result(self):
        self._evt.wait()
        return self._result
class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r
    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))

worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())
