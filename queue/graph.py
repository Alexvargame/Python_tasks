from typing import NamedTuple
import networkx as nx
from collections import deque
from math import infinity
from queues import MutableMinHeap, Queue, Stack
class City(NamedTuple):
    name: str
    country: str
    year: int#|None
    latitude: float
    longtude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longtude=float(attrs["longtude"]),
        )
def load_graph(filename, node_factory):
    graph=nx.nx_agraph.read_dot(filename)
    nodes={
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
        )
def retrace(previous, source, destination):
    path=deque()

    current=destination
    while current!=source:
        path.appendleft(current)
        current=previous.get(current)
        if current is None:
            return None
    path.appendleft(source)
    return list(path)
def shortest_path(graph, source, destination, order_by=None):
    queue=Queue(source)
    visited={source}
    previous={}
    for node in queue:
        node=queue.dequeue()
        yield node
        neighbors=list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                previous[neighbor]=node
                if neighbor==destination:
                    return retrace(previous, source, destination)
def breadth_first_traverse(graph, source, order_by=None):
    queue=Queue(source)
    visited={source}
    
    for node in queue:
        yield node
        neighbors=list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
def breadth_first_search(graph, source, predicate, order_by=None):
    return search (breadth_first_traverse, graph, source, order_by)
def depth_first_search(graph, source, predicate, order_by=None):
    return search(depth_first_traverse, graph, source, predicate, order_by)

def search(traverse, graph, source, predicate, order_by=None):
    for node in traverse(graph, source, order_by):
        if predicate(node):
            return node
       
def connected(graph, source, destination):
    return shortest_path(graph, source, destination) is not None
def depth_first_traverse(graph, source, order_by=None):
    stack = Stack(source)
    visited = set()
    while stack:
        if (node := stack.dequeue()) not in visited:
            yield node
            visited.add(node)
            neighbors = list(graph.neighbors(node))
            if order_by:
                neighbors.sort(key=order_by)
            for neighbor in reversed(neighbors):
                stack.enqueue(neighbor)
def recursive_depth_first_traverse(graph, source, order_by=None):
    visited = set()

    def visit(node):
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                yield from visit(neighbor)

    return visit(source)
def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous={}
    visited=set()

    unvisited=MutableMinHeap()
    for node in graph.nodes:
        unvisited[node]= infinity
        unvesited[source]= 0
    while unvisited:
        visited.add(node =unvisited.dequeue())
        for neighbor not in visited:
            weight=weight_factory(weights)
            new_distance=unvisited[node]+weight
            if new_distance<unvisited[neighbor]:
                unvisited[neighbor]=new_distance
                previous[neighbor]=node
    return retrace(previous, source, dectination)
        

    
