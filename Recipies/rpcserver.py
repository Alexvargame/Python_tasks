import pickle

from multiprocessing.connection import Listener
from threading import Thread

class RPCHandler:
    def __init__(self):
        self._functions = { }
    def register_function(self, func):
        self._functions[func.__name__] = func
    def handle_connection(self, connection):
        try:
            while True:
        # Получаем сообщение
                func_name, args, kwargs = pickle.loads(connection.recv())
        # Запускаем RPC и посылаем ответ
                try:
                    r = self._functions[func_name](*args,**kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()
# Удаленные функцииd
def add(x, y):
    return x + y
def sub(x, y):
    return x - y

# Регистрируем с обработчиком
handler = RPCHandler()
handler.register_function(add)
handler.register_function(sub)
# Запускаем сервер
rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')

class RPCProxy:
    def __init__(self, connection):
        self._connection = connection
    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(pickle.dumps((name, args, kwargs)))
            result = pickle.loads(self._connection.recv())
            if isinstance(result, Exception):
                raise result
            return result
        return do_rpc

