
from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar,Generic,List
from heapq import heappop,heappush


T=TypeVar('T')
V=TypeVar('V')
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container
    def push(self,item):
        heappush(self._container,item)
    def pop(self):
        return heappop(self._container)
    def __repr__(self):
        return repr(self._container)
@dataclass
class DijkstraNode:
    vertex:int
    distance:float

    def __lt__(self, other):
        return self.distance<other.distance
    def __eq__(self, other):
        return self.distance==other.distance


@dataclass
class WeightedEdge:
    u:int
    v:int
    weight:float

    def reversed(self):
        return WeightedEdge(self.v,self.u,self.weight)
    def __lt__(self, other):
        return self.weight<other.weight

    def __str__(self):
        return f'{self.u} {self.weight} -> {self.v}'
    
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

    #Добвляем вершины в обоиз направлениях
    def add_edge(self,edge):
        self._edges[edge.u].append(edge)
        #self._edges[edge.v].append(edge.reversed())
    #Добавляем ребро, используя индексы вершин
    def add_edge_by_indices(self,u,v,weight):
        edge=WeightedEdge(u,v,weight)
        self.add_edge(edge)
    #Добавляем ребро, просамтривая индексы вершин
    def add_edge_by_vertices(self,first,second,weight):
        u=self._vertices.index(first)
        v=self._vertices.index(second)
        self.add_edge_by_indices(u,v,weight)

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
    def neighbors_for_index_with_weight(self,index):
        distance_tuples=[]
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v),edge.weight))
        return distance_tuples
    def __str__(self):
        desc=''
        for i in range(self.vertex_count):
            desc+=f"{self.vertex_at(i)}->{self.neighbors_for_index_with_weight(i)}\n"
        return desc
    
def graph(pyramid):
    print (pyramid)
    gr=[[((i,j),pyramid[i][j]) for j in range(len(pyramid[i]))] for i in range(len(pyramid))]
    gr1=[item for sublist in gr for item in sublist]
    graph1=Graph([g[0] for g in gr1])
    for i in range(len(gr)-1):
        for j in range(len(gr[i])):
            graph1.add_edge_by_vertices(gr[i][j][0],gr[i+1][j][0],gr[i+1][j][1])
            graph1.add_edge_by_vertices(gr[i][j][0],gr[i+1][j+1][0],gr[i+1][j+1][1])
    return graph1

def dijkstra(wg,root):
    print('re',wg,root)
    first=wg.index_of(root[0])
    distances=[None]*wg.vertex_count
    distances[first]=root[1]
    path_dict={}
    pq=PriorityQueue()
    pq.push(DijkstraNode(first,0))

    while not pq.empty:
        u=pq.pop().vertex
        dist_u=distances[u]
        for we in wg.edges_for_index(u):
            dist_v=distances[we.v]
            if dist_v is None or dist_v<we.weight+dist_u:
                distances[we.v]=we.weight+dist_u
                path_dict[we.v]=we
                pq.push(DijkstraNode(we.v,we.weight+dist_u))
    return distances,path_dict
    
def path_to_dict(start,end,path_dict):
    if (len(path_dict))==0:
        return []
    edge_path=[]
    e=path_dict[end]
    edge_path.append(e)
    while e.u!=start:
        e=path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))

    
def main():

    pyramid=[[3],[7,4],[2,4,6],[8,5,9,3]]
    graph1=graph(pyramid)
    sums,path_dict=dijkstra(graph1,((0,0),pyramid[0][0]))
    print(sums) 
    path=path_to_dict(graph1.index_of((0,0)),graph1.index_of((3,2)),path_dict)
    print(path)

if __name__ == "__main__":
    main()

#
