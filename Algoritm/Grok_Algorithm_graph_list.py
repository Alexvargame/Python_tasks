from collections import deque

graph={}
graph['Проснуться']=['Принять душ','Почистить зубы']
graph['Почистить зубы']=['Позавтракать']
graph['Принять душ']={}
graph['Позавтракать']={}

list1=['Проснуться','Принять душ','Позавтракать','Почистить зубы']

print(graph)

def search(name):
    search_queue=deque()
    search_queue+=graph['Проснуться']
    searched=[]
    searched.append(name)
    while search_queue:
        end_point=search_queue.popleft()
        if not end_point in searched:
                print(end_point)
##            if end_point==name:
##                return True
##            else:
                search_queue+=graph[end_point]
                searched.append(end_point)
    print(searched)
    return searched==list1

print(search('Проснуться'))
    
def main():
    pass



if __name__ == "__main__":
    main()




#
