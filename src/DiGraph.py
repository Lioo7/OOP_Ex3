from src.GraphInterface import GraphInterface
from src.node_data import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.nodes_Neighbors = {}
        self.count_edges = 0
        self.mc = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.count_edges

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """

        :param id1:
        :return:
        """
        temp = {}
        if id1 in self.nodes:
            return self.nodes.get(id1)
        else:
            return temp

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = NodeData(node_id, pos)
            self.nodes_Neighbors[id] = {}
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:

        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass
