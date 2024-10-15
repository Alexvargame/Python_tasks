from queues import Queue
from queues import Stack
from queues import PriorityQueue
from heapq import heappush, heappop


fifo=Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print(fifo._elements)
for element in fifo:
    print(element)
    
print(len(fifo))

lifo=Stack("1", "2", "3")
for element in lifo:
    print(element)
 

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")
print(fruits)
heappop(fruits)
print(fruits)

person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

print(person1<person2, person2<person3)
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())
print(messages.dequeue())

