import argparse
from queues import Queue, PriorityQueue#, LifoQueue
import threading
from random import randint, choice
from time import sleep

QUEUE_TYPES={
    'fifo':Queue,
    #'lifo':LifoQueue,
    'heap':PriorityQueue
    }
PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)
class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0
    @property
    def state(self):
        if self.working:
            return f"{self.product}({self.progress}%)"
        return ":zzz:Idle"

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))
        
    def simulate_work(self):
       
        self.working = True
        self.progress = 0
        delay =randint(1,1+15//self.speed)
        for _ in range(100):
            sleep(delay/100)
            self.progress+=1
            
class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products

    def run(self):
        while True:
            self.product = choice(self.products)
            self.simulate_work()
           
            self.buffer.put(self.product)
            self.simulate_idle()
            
    @property
    def state(self):
        if self.working:
            return f"{self.product}({self.progress}%)"
        return ":zzz:Idle"

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))
        
    def simulate_work(self):
       
        self.working = True
        self.progress = 0
        delay =randint(1,1+15//self.speed)
        for _ in range(100):
            sleep(delay/100)
            self.progress+=1

class Consumer(Worker):
    def run(self):
        while True:
            self.product = self.buffer.get()
            self.simulate_work()
            self.buffer.task_done()
            self.simulate_idle()
    @property
    def state(self):
        if self.working:
            return f"{self.product}({self.progress}%)"
        return ":zzz:Idle"

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))
        
    def simulate_work(self):
       
        self.working = True
        self.progress = 0
        delay =randint(1,1+15//self.speed)
        for _ in range(100):
            sleep(delay/100)
            self.progress+=1

def main(args):
    buffer=QUEUE_TYPES[args.queue]()
    print(type(buffer))

    producers=[Producer(args.producer_speed, buffer, PRODUCTS) for _ in range(args.producers)]
    consumers=[Consumer(args.consumer_speed, buffer) for _ in range(args.producers)]


    for producer in producers:
        producer.start()
    for consumer in consumers:
        consumer.start()

    view=View(buffer, producers, consumers)
    view.animate()



def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-q','--queue',choices=QUEUE_TYPES, default='fifo')
    parser.add_argument('-p','--producers',type=int, default=3)
    parser.add_argument('-c','--consumers',type=int, default=2)
    parser.add_argument('-ps','--producer-speed',type=int, default=1)
    parser.add_argument('-cs','--consumer-speed',type=int, default=1)
    return parser.parse_args()

if __name__=='__main__':
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass
