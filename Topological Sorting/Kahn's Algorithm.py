class Node:
    def __init__(self, value):
        self.value = value
        self.in_degree = 0
        self.out_nodes = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.nodes:
            self.nodes[from_node] = Node(from_node)
        if to_node not in self.nodes:
            self.nodes[to_node] = Node(to_node)

        self.nodes[from_node].out_nodes.append(self.nodes[to_node])
        self.nodes[to_node].in_degree += 1
    
def kahn_topological_sort(graph):
    sorted_list = []
    zero_in_degree_nodes = [node for node in graph.nodes.values() if node.in_degree == 0]

    while zero_in_degree_nodes:
        current_node = zero_in_degree_nodes.pop(0)
        sorted_list.append(current_node.value)

        for neighbor in current_node.out_nodes:
            neighbor.in_degree -= 1
            if neighbor.in_degree == 0:
                zero_in_degree_nodes.append(neighbor)

    if len(sorted_list) != len(graph.nodes):
        raise ValueError("Graph has at least one cycle, topological sort not possible.")
    
    return sorted_list

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    sorted_nodes = kahn_topological_sort(graph)
    print("Topological Sort:", sorted_nodes) 