from edge import Edge
from typing import TypeVar,Generic,List,Optional
from generic_search import bfs,node_to_path,Node

V=TypeVar('V')


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


def main():
    city_graph= Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
            "New Vork", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New Vork")
    city_graph.add_edge_by_vertices("Boston", "New Vork")
    city_graph.add_edge_by_vertices("New Vork", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)
    # city_graph.del_vertex('Riverside')
    # city_graph.del_edge('Chicago','Dallas')
    # print('c',city_graph)
    begin_path='Boston'
    end_path='Phoenix'
    bfs_result=bfs(begin_path,lambda x:x==end_path,city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print('No solution')
    else:
        path=node_to_path(bfs_result)
        print(f"Path from {begin_path} to {end_path}:")
        print(path)




if __name__=="__main__":
    main()
