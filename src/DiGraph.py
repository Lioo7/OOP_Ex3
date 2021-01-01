from edge_data import EdgeData
from src.GraphInterface import GraphInterface
from src.node_data import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.count_edges = 0
        self.mc = 0


def v_size(self) -> int:
    return len(self.nodes)


def e_size(self) -> int:
    return self.count_edges


def get_all_v(self) -> dict:
    return self.nodes


def all_in_edges_of_node(self, id1: int) -> dict:
    for node in self.


def all_out_edges_of_node(self, id1: int) -> dict:
    pass


def get_mc(self) -> int:
    return self.mc


def add_edge(self, id1: int, id2: int, weight: float) -> bool:
    # Checks if the nodes are not equal and if the wight is valid
    if id1 != id2 and weight > 0:
        # Checks if the nodes exist in the nodes dictionary
        if id1 and id2 in self.nodes.keys():
            # Checks if the edge does not exist already
            if id1 and id2 not in self.edges:
                # Creates a new edge and add it to the edge dictionary
                edge = EdgeData(id1, id2, weight)
                self.edges[id1][id2] = edge
                # Increments the count_edges by one
                self.count_edges += 1
                # Increments the mc by one
                self.mc += 1
                return True


def add_node(self, node_id: int, pos: tuple = None) -> bool:
    # Checks if the node does not exist already
    if node_id in self.nodes.keys():
        return False
    else:
        # Creates a new node and adds it to the nodes dictionary
        self.nodes[node_id] = NodeData(node_id, pos)
        # Creates an empty inner dictionary in edges
        self.edges.setdefault(node_id, {})
        # Increments the mc by one
        self.mc += 1
    return True


def remove_node(self, node_id: int) -> bool:
    pass


def remove_edge(self, node_id1: int, node_id2: int) -> bool:
    pass
