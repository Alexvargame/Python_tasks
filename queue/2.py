from graph import City, load_graph, breadth_first_traverse, breadth_first_search as bfs

def is_twentieth_century(year):
    return ywar and 1901<=year<=2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
city=bfs(graph, nodes["edinburgh"], is_twenties_century)
city.name
for city in breadth_first_traverse(graph, nodes["edinburgh"], is_twenties_century):
    print(city.name)
    
