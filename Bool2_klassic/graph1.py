from typing import TypeVar, Generic, List, Optional
from edge import Edge
from generic_search import bfs, Node, node_to_path

V=TypeVar('V')



class Graph(Generic[V]):
    def __init__(self, vertices):
        self._vertices=vertices
        self._edges=[[] for _ in vertices]

    @property
    def vertex_count(self):
        return len(self._vertices)
    @property
    def edge_count(self):
        return sum(map(len,self._edges))

    def add_vertex(self, vertex):
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count-1

    def add_edge(self, edge):
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u,v):
        edge=Edge(u,v)
        self.add_edge(edge)
    def add_edge_by_vertices(self,first, second):
        u=self._vertices.index(first)
        v=self._vertices.index(second)
        self.add_edge_by_indices(u,v)

    def vertex_at(self, index):
        return self._vertices[index]

    def index_of(self,vertex):
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self,vertex):
        return self.neighbors_for_index(self.index_of(vertex))
    def edges_for_index(self, index):
        return self._edges[index]
    def eges_for_vertex(self, vertex):
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self):
        desc=''
        for i in range(self.vertex_count):
            desc+=f"{self.vertex_at(i)}->{self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
    dict_list=[]
    for n in list(set(net)):
        dict_list.extend(list(n))
    print(list(set(dict_list)))
# тест простейшей графобой конструкции
    p_graph= Graph(list(set(dict_list)))
    
    for n in net:
        p_graph.add_edge_by_vertices(n[0],n[1])
    
    print(p_graph) 
    bfs_result=bfs("Boston", lambda x:x=='Miami', city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print('No solution found using breadth-first search!')
    else:
        path=node_to_path(bfs_result)
        print("Path from Boston to Miami:")
        print(path)
    bfs_result=bfs("Boston", lambda x:x=='Houston', city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print('No solution found using breadth-first search!')
    else:
        path=node_to_path(bfs_result)
        print("Path from Boston to Houston:")
        print(path)
