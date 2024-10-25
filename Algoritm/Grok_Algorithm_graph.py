from collections import deque

graph={}
graph['Проснуться']=['Принять душ','Почистить зубы']
graph['Почистить зубы']=['Позавтракать']


print(graph)

def search(name):
    search_queue=deque()
    search_queue+=graph['S']
    searched=[]
    while search_queue:
        end_point=search_queue.popleft()
        if not end_point in searched:
            print(end_point)
            if end_point==name:
                return True
            else:
                search_queue+=graph[end_point]
                searched.append(end_point)
    return False

print(search('F'))
    
def main():
    pass



if __name__ == "__main__":
    main()




#
