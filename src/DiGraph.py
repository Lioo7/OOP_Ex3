from src.GraphInterface import GraphInterface
from src.NodeData import NodeData


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.Neighbors_in = {}
        self.Neighbors_out = {}
        self.count_edges = 0
        self.mc = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
          Returns the number of edges in this graph
          @return: The number of edges in this graph
          """
        return self.count_edges

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph,
        each node is represented using apair  (key, node_data)"""
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id,
         each node is represented using a pair (key, weight)"""
        return self.Neighbors_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id,
        each node is represented using a pair (key, weight)"""
        return self.Neighbors_out.get(id1)

    def get_mc(self) -> int:
        """
            Returns the current version of this graph,
            on every change in the graph state - the MC should be increased
            @return: The current version of this graph.
            """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        ans = False
        # Checks if the ids exist and are not equal to each other
        if id1 in self.nodes and id2 in self.nodes and id1 != id2:
            # Checks that the edge does not already exist
            if id1 not in self.Neighbors_in[id2] and weight > 0:
                self.Neighbors_out[id1][id2] = weight
                self.Neighbors_in[id2][id1] = weight
                self.count_edges += 1
                self.mc += 1
                ans = True

        return ans

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        # Checks if the node does not exist already
        if node_id in self.nodes.keys():
            return False
        else:
            # Creates a new node and adds it to the nodes dictionary
            self.nodes[node_id] = NodeData(node_id, pos)
            # Creates an empty inner dictionary in Neighbors_in
            self.Neighbors_in[node_id] = {}
            # Creates an empty inner dictionary in Neighbors_out
            self.Neighbors_out[node_id] = {}
            # Increments the mc by one
            self.mc += 1
        return True

    """"
    This function gets a node's key and returns the NodeData
    """

    def get_node(self, node_id: int) -> NodeData:
        if node_id in self.nodes.keys():
            return self.nodes.get(node_id)
        else:
            return None

    def remove_node(self, node_id: int) -> bool:
        """
             Removes a node from the graph.
             @param node_id: The node ID
             @return: True if the node was removed successfully, False o.w.
             Note: if the node id does not exists the function will do nothing
             """
        # Check if the node exist
        if node_id in self.nodes:
            # Go through the list of all the nodes that have an edge to node_id
            for i in self.Neighbors_in.get(node_id):
                del self.Neighbors_in[i][node_id]
                # self.mc += 1
                self.count_edges -= 1
            # Go through the list of all the nodes that have an edge from node_id
            for i in self.Neighbors_out.get(node_id):
                del self.Neighbors_out[i][node_id]
                # self.mc += 1
                self.count_edges -= 1

            del self.nodes[node_id]
            del self.Neighbors_in[node_id]
            del self.Neighbors_out[node_id]
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
         Removes an edge from the graph.
         @param node_id1: The start node of the edge
         @param node_id2: The end node of the edge
         @return: True if the edge was removed successfully, False o.w.
         Note: If such an edge does not exists the function will do nothing
         """
        # Check if the nodes exist
        if node_id1 in self.nodes and node_id2 in self.nodes:
            # Check if the edge exist
            if node_id2 in self.Neighbors_out[node_id1]:
                del self.Neighbors_in[node_id2][node_id1]
                del self.Neighbors_out[node_id1][node_id2]
                self.count_edges -= 1
                self.mc += 1
                return True
            return False
        return False

    def __repr__(self):
        edges = []
        for src in self.nodes.keys():
            for dest in self.all_in_edges_of_node(src).keys():
                w = self.all_in_edges_of_node(src)[dest]
                edges.append({"src": src, "w": w, "dest":dest})
        s = "Edges={}\nNodes=[{}]\n".format(edges, self.nodes)
        return s

    def __eq__(self, other):

        return self.nodes == other.nodes and self.Neighbors_in == other.Neighbors_in\
               and self.Neighbors_out == other.Neighbors_out and self.count_edges == other.count_edges

