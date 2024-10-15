import time
from functools import wraps, partial
import logging

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper



# Вспомогательный декоратор для прикрепления
# к функции в качестве атрибута obj

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level,name=None,message=None):

    def decorate(func):
        logname=name if name else func.__module__
        log=logging.getLogger(logname)
        logmsg=message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            print(level,logmsg)
            return func(*args,**kwargs)
        # Прикрепляем функции-сеттеры
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
            print(level,logmsg)
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
            print(level,logmsg)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')
        
        
add(2,3)
add.set_message('!!!')
spam()

@timethis
@logged(logging.DEBUG)
def countdown(n):
    
    while n>0:
        n-=1
countdown(100000)
