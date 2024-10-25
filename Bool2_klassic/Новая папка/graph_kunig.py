from edge import Edge
from typing import TypeVar,Generic,List,Optional
from generic_search import node_to_path,Node
from collections import deque

V=TypeVar('V')
T=TypeVar('T')
class Queue(Generic[T]):
    def __init__(self):
        self._container=deque()
    @property
    def empty(self):
        return not self._container

    def push(self,item):
        self._container.append(item)
    def pop(self):
        return self._container.popleft()
    def __repr__(self):
        return repr(self._container)

class Graph(Generic[V]):
    def __init__(self,vertices=[]):
        self._vertices=vertices
        self._edges=[[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)
    @property
    def edge_count(self):
        return sum(map(len,self._edges))
    #Добавляем вершину и возвращаем индекс
    def add_vertex(self,vertex):
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count-1

    # Удаляеим вершину
    def del_vertex(self, vertex):
        for edge in self.edges_for_vertex(vertex)[::-1]:
            self._edges[edge.u].remove(edge)
            self._edges[edge.v].remove(edge.reversed())
    def del_edge(self, first,second):
        print(self.index_of(first),self.index_of(second))
        edge=Edge(self.index_of(first),self.index_of(second))
        self._edges[Edge(self.index_of(first),self.index_of(second)).u].remove(Edge(self.index_of(first),self.index_of(second)))
        self._edges[Edge(self.index_of(first),self.index_of(second)).v].remove(Edge(self.index_of(first),self.index_of(second)).reversed())


    def del_edge_by_vertex(self,vertex,other):
        u=self._vertices.index(vertex)
        v=self._vertices.index(other)
        print(Edge(u,v))
    #Добвляем вершины в обоиз направлениях
    def add_edge(self,edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())
    #Добавляем ребро, используя индексы вершин
    def add_edge_by_indices(self,u,v):
        edge=Edge(u,v)
        self.add_edge(edge)
    #Добавляем ребро, просамтривая индексы вершин
    def add_edge_by_vertices(self,first,second):
        u=self._vertices.index(first)
        v=self._vertices.index(second)
        self.add_edge_by_indices(u,v)

    #Поиск вершины по индексу
    def vertex_at(self,index):
        return self._vertices[index]

    #Поиск вершины в графе
    def index_of(self,vertex):
        return self._vertices.index(vertex)

    #Поиск вершин, с которыми связана вершина с заданным индексом
    def neighbors_for_index(self,index):
        return list(map(self.vertex_at,[e.v for e in self._edges[index]]))
    #Поиск индекса вершины, возращает ее соседей
    def neighbors_for_vertex(self,vertex):
        return self.neighbors_for_index(self.index_of(vertex))
    #Возвращает ребра, связанные с вершиной, имеющей заданный индекс
    def edges_for_index(self,index):
        return self._edges[index]
    #Поиск индекса вершины, возвращает ее ребра
    def edges_for_vertex(self,vertex):
        return self.edges_for_index(self.index_of(vertex))
    def __str__(self):
        desc=''
        for i in range(self.vertex_count):
            desc+=f"{self.vertex_at(i)}->{self.neighbors_for_index(i)}\n"
        return desc
def bfs(initial,goal_test,successors):
    frontier=Queue()
    frontier.push(Node(initial,None))
    explored={initial}
    edges = []
    for m in goal_test:
        edges.extend(m)

    print(edges)
    edges.remove(Edge(u=2, v=4))
    edges.remove(Edge(u=4, v=2))
    print(edges)
    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        if len(edges)==0:
            return current_node
        print(successors(current_state))
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,current_node))
            print('EEE',current_node)
    return None

# def goal_test(lst):
#     if len(lst)==0:
#         return True
#     return False

def main():
    city_graph= Graph(["Island A", "Island B", "Island C1", "Island D","Island C2"])
    city_graph.add_edge_by_vertices("Island A", "Island B")
    city_graph.add_edge_by_vertices("Island A", "Island D")
    city_graph.add_edge_by_vertices("Island A", "Island C1")
    city_graph.add_edge_by_vertices("Island B", "Island C1")
    city_graph.add_edge_by_vertices("Island B", "Island C2")
    city_graph.add_edge_by_vertices("Island D", "Island C1")
    city_graph.add_edge_by_vertices("Island B", "Island C2")
    city_graph.add_edge_by_vertices("Island C1", "Island C2")

    print(city_graph)
    print(city_graph._edges)

    # city_graph.del_vertex('Riverside')
    # city_graph.del_edge('Chicago','Dallas')
    # print('c',city_graph)
    begin_path='Island A'
    end_path='Island C1'
    bfs_result=bfs(begin_path,city_graph._edges,city_graph.neighbors_for_vertex)

    if bfs_result is None:
        print('No solution')
    else:
        path=node_to_path(bfs_result)
        print(f"Path from {begin_path} to {end_path}:")
        print(path)




if __name__=="__main__":
    main()
