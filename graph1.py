class SimpleGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = set()
    def insert_node(self,node):
        if node not in self.nodes:
            self.nodes[node] = set()
            print(f"Node {node} inserted.")
        else:
            print(f"Node{node} already exists.")
    def insert_edge(self,node1,node2):
        if node1 in self.nodes and node2 in self.nodes:
            edge = (node1,node2) if node1 < node2 else(node2,node1):
            
