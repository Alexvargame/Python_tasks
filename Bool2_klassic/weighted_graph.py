from typing import TypeVar, Generic, List, Optional
from weighted_edge import WeightedEdge
from graph import Graph

V=TypeVar('V')



class WeightedGraph(Generic[V],Graph[V]):
    def __init__(self, vertices):
        self._vertices=vertices
        self._edges=[[] for _ in vertices]

    def add_edge_by_indices(self, u,v, weight):
        edge=WeightedEdge(u,v, weight)
        self.add_edge(edge)
    def add_edge_by_vertices(self,first, second, weight):
        u=self._vertices.index(first)
        v=self._vertices.index(second)
        self.add_edge_by_indices(u,v, weight)

    

    def neighbors_for_index_with_weights(self,index):
        distance_tuples=[]
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        
        return distance_tuples

    
    def __str__(self):
        desc=''
        for i in range(self.vertex_count):
            desc+=f"{self.vertex_at(i)}->{self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == "__main__":
# тест простейшей графобой конструкции
    city_graph2= WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York",
    "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
    "Washington"]) 
    city_graph2.add_edge_by_vertices("Seattle", "Chicago",1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco",678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside",386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles",348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside",50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix",357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix",307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago",1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston",1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago",805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta",721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston",225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta",702)
    city_graph2.add_edge_by_vertices("Houston", "Miami",968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago",558)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington",543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami",604)
    city_graph2.add_edge_by_vertices("Miami", "Washington",923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit",238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston",613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington",396)
    city_graph2.add_edge_by_vertices("Detroit", "New York",482)
    city_graph2.add_edge_by_vertices("Boston", "New York",190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia",81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington",123)
    print(city_graph2) 
##    bfs_result=bfs("Boston", lambda x:x=='Miami', city_graph.neighbors_for_vertex)
##    if bfs_result is None:
##        print('No solution found using breadth-first search!')
##    else:
##        path=node_to_path(bfs_result)
##        print("Path from Boston to Miami:")
##        print(path)
##    bfs_result=bfs("Boston", lambda x:x=='Houston', city_graph.neighbors_for_vertex)
##    if bfs_result is None:
##        print('No solution found using breadth-first search!')
##    else:
##        path=node_to_path(bfs_result)
##        print("Path from Boston to Houston:")
##        print(path)
