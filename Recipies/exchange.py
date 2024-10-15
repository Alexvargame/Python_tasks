from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()
    def attach(self, task):
        self._subscribers.add(task)
    def detach(self, task):
        self._subscribers.remove(task)
    def send(self, msg):

        for subscriber in self._subscribers:
            subscriber.send(msg)
    # Словарь всех созданных пунктов обмена
_exchanges = defaultdict(Exchange)
    # Вернуть экземпляр Exchange, ассоциированный с переданным именем
def get_exchange(name):
    return _exchanges[name]
class Task:
    def __init__(self,name):
        self.name=name
     
    def send(self, msg):
        print(msg)
task_a = Task('A')
task_b = Task('B')
# Пример получения пункта обмена
exc = get_exchange('name')
print(exc._subscribers)
# Пример подписывания задач на него
exc.attach(task_a)
exc.attach(task_b)
for sub in exc._subscribers:
    print(sub.name)

# Пример отсылки сообщений
exc.send('msg1')
exc.send('msg2')
# Пример отписки
exc.detach(task_a)
exc.detach(task_b)

