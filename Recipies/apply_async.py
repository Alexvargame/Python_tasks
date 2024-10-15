def apply_async(func, args,*,callback):
    result=func(*args)
    callback(result)


def print_result(result):
    print('got:',result)

def add(x,y):
    return x + y

class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self,result):
        self.sequence+=1
        print('[{}] Got:{}'.format(self.sequence,result))


        
apply_async(add,(2,3),callback=print_result)
r=ResultHandler()
apply_async(add,(2,3),callback=r.handler)
