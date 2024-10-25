from __future__ import annotations
from typing import TypeVar, List,Dict,Optional,Tuple
from dataclasses import dataclass
from mst import WeightedPath,print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue


V=TypeVar('V')
@dataclass
class DijkstraNode:
    vertex:int
    distance:float

    def __lt__(self, other):
        return self.distance<other.distance
    def __eq__(self, other):
        return self.distance==other.distance

def dijkstra(wg,root):
    first=wg.index_of(root)
    distances=[None]*wg.vertex_count
    distances[first]=0
    path_dict={}
    pq=PriorityQueue()
    pq.push(DijkstraNode(first,0))

    while not pq.empty:
        u=pq.pop().vertex
        dist_u=distances[u]
        for we in wg.edges_for_index(u):
            dist_v=distances[we.v]
            if dist_v is None or dist_v>we.weight+dist_u:
                distances[we.v]=we.weight+dist_u
                path_dict[we.v]=we
                pq.push(DijkstraNode(we.v,we.weight+dist_u))
    return distances,path_dict

def distance_array_to_vertex_dict(wg,distances):
    distance_dict={}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)]=distances[i]
    return distance_dict
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
    city_graph2 = WeightedGraph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                                 "New Vork", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                 "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New Vork", 482)
    city_graph2.add_edge_by_vertices("Boston", "New Vork", 190)
    city_graph2.add_edge_by_vertices("New Vork", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    start='Los Angeles'
    end='Boston'
    distances,path_dict=dijkstra(city_graph2,start)
    name_distance=distance_array_to_vertex_dict(city_graph2,distances)
    print(f"Distance from {start}:")
    for key, value in name_distance.items():
        print (f"{key}->{value}")

    print(f"Shortest path from {start} to {end}:")
    path=path_to_dict(city_graph2.index_of(start),city_graph2.index_of(end),path_dict)
    print_weighted_path(city_graph2,path)


if __name__=="__main__":

    main()





