from collections import deque

graph={}
graph['you']=['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph ['alice'] = [ 'peggy' ]
graph ['claire'] = ['thom', 'jonny']
graph ['anuj'] = [ ]
graph ['peggy'] = []
graph ['thom'] = [ ]
graph ['jonny'] = []
print(graph)

def person_is_seller(name):
    
    return len(name)==4

def search(name):
    print(graph['you'])
    search_queue=deque()
    print(search_queue)
    search_queue+=graph['you']
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        print(person)
        input()
        
        if not person in searched:
            if person_is_seller(person):
                print(person+"  is seller")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
        print(searched)
    return False

search("you")
