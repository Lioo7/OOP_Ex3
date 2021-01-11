import json
from queue import PriorityQueue
from typing import List
from DiGraph import DiGraph
from NodeData import NodeData
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from matplotlib import pyplot as plt
from random import uniform


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name, "r") as read_file:
                json_graph = json.load(read_file)
                graph = DiGraph()
            for n in json_graph["Nodes"]:
                if "pos" not in n:
                    graph.add_node(n["id"])
                else:
                    pos = eval(str(n["pos"]))  # convert string to tuple
                    graph.add_node(n["id"], pos)

            for e in json_graph["Edges"]:
                graph.add_edge(e["src"], e["dest"], e["w"])
            self.graph = graph
            return True
        except Exception as exception:
            print(exception)
            return False
        finally:
            read_file.close()

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        try:
            with open('../data/' + file_name, "w") as write_file:
                json_graph = {"Edges": [], "Nodes": []}
                # save edges as json
                for id1 in self.graph.Neighbors_out.keys():
                    for id2, w in self.graph.all_out_edges_of_node(id1).items():
                        json_graph["Edges"].append({"src": id1, "w": w, "dest": id2})
                # save nodes as json
                for n in self.graph.nodes.values():
                    if n.pos is None:
                        json_graph["Nodes"].append({"id": n.key})
                    else:
                        json_graph["Nodes"].append({"pos": str(n.pos)[1: -1], "id": n.key})
                json.dump(json_graph, write_file)
            return True
        except Exception as e:
            print("Exception: ",e)
            return False
        finally:
            write_file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        # Checking if the keys exist
        if id1 not in self.graph.nodes.keys() or id2 not in self.graph.nodes.keys():
            return float('inf'), []
        if id1 == id2:
            return float('inf'), []
        if self.shortest_path_distance(id1, id2) == -1:
            return float('inf'), []

        """
        Calls the dijkstra method to check if there exists a pathway between both of the given nodes.
        If the dijkstra function returned a positive number, then adds all the numbers in the info of
        the destination node to the list (by calling isNumeric method).
        Then adds the destination node to the list and returns the path.
        """
        path = []
        distance = self.shortest_path_distance(id1, id2)
        if distance > -1:
            destination = self.graph.get_node(id2)
            string = destination.get_info()
            arr = string.split("->")
            for temp in arr:
                if self.is_numeric(temp):
                    key = int(temp)
                    path.append(key)

            path.append(id2)
            return distance, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        # If the graph is None or id1 is not in the graph, return an empty list []

        if self.graph is None or id1 not in self.graph.nodes.keys():
            return []
        ssc = [id1]
        # Go over all the key's nodes in the graph
        for key in self.graph.get_all_v().keys():
            # If there is a path between id1 to key and also to the opposite direction
            if id1 != key and self.shortest_path_distance(id1, key) != -1 and \
                    self.shortest_path_distance(key, id1) != -1:
                ssc.append(key)
        return ssc

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        # If the graph is None, return an empty list []
        if self.graph is None:
            return []
        all_covered = []
        # Resets all the tags to zero
        for key in self.graph.get_all_v().keys():
            self.graph.get_node(key).set_tag(0)
        all_scc = []
        # Go over all the key's nodes in the graph
        for key in self.graph.get_all_v().keys():
            if key not in all_covered:  # the key is not in a scc yet
                scc_key = self.connected_component(key)
                for node in scc_key:
                    all_covered.append(node)
                all_scc.append(scc_key)
        return all_scc

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        head_width = 0.05  # vertex's width
        min_x = min_y = 0  # the lower limit of the random float
        max_x = max_y = 1000  # the upper limit of the random float
        x_nodes_list = []  # X-axis of the vertices
        y_nodes_list = []  # y-axis of the vertices
        key_list = []  # contains all the keys in the graph

        # traverses the vertices list
        for key in self.get_graph().get_all_v():
            node = self.graph.get_node(key)
            pos_node = node.get_pos()
            # if the node does not have a position, placed in a random position
            if pos_node is None:
                x_node = uniform(min_x, max_x)
                y_node = uniform(min_y, max_y)
                # Sets the node's position
                new_pos = (x_node, y_node)
                node.set_pos(new_pos)
            # otherwise, the node will be placed in its original position
            else:
                x_node = pos_node[0]
                y_node = pos_node[1]

            # adds the x and the y of each vertex to the lists
            x_nodes_list.append(x_node)
            y_nodes_list.append(y_node)
            key_list.append(key)

        # drawing vertices: (x, y)
        plt.scatter(x_nodes_list, y_nodes_list)

        # drawing key's number: key num | (x-gap,y+gap)
        for i in range(0, len(key_list)):
            plt.annotate(key_list[i], (x_nodes_list[i] - 3.3, y_nodes_list[i] + 12))

        # traverses the edges
        for src in self.graph.get_all_v().values():
            for dest_key in self.graph.all_out_edges_of_node(src.get_key()).keys():
                dest_node = self.graph.get_node(dest_key)
                dest_x = dest_node.get_pos()[0] - src.get_pos()[0]
                dest_y = dest_node.get_pos()[1] - src.get_pos()[1]
                src_x = src.get_pos()[0]
                src_y = src.get_pos()[1]

                # drawing edges: dx(src) | dy(dest) | head width
                plt.arrow(src_x, src_y, dest_x - head_width, dest_y - head_width, head_width=head_width)

        # adds a title
        plt.title("DiGraph")
        plt.show()

    # ======HELPFUL FUNCTIONS====== #

    def clear(self):
        """
        Clears the graph  and initializes all the nodes in the graph to their default values.
        :return: None
        """
        for key in self.graph.get_all_v().keys():
            node = self.graph.get_node(key)
            node.set_info("")
            node.set_tag(0)
            node.set_weight(float('inf'))

    def dijkstra(self, source):
        """
        The Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.
        For a given source node in the graph, the algorithm finds the shortest path between that node and every other.
        :param source: the source node
        :return: None
        """

        # Clears the graph
        self.clear()

        # Sets the source node values to zero
        src = self.graph.get_node(source)
        src.set_tag(0)
        src.set_weight(0)

        # Creates a priority queue which will contain the nodes that need to traverse.
        # The priority queue ranks the nodes by their tag values from the greater to the lesser.
        pq = PriorityQueue(maxsize=self.graph.v_size())
        pq.put((src.get_tag(), src))

        """
        While the p.queue is not empty, the algorithm takes the first node marks it and traverses
        all its neighbors(all the destinations of the node).
        If this neighbor is not yet visited it calculates its distance from the source.
        If its distance is smaller than its tag value, then sets its tag to be distance
        and set its info to contain the path from the source till this node. Then adds this node to the p.queue.
        After the algorithm finishes gaining with all the neighbors, it continues to the next node in the p.queue.
        """
        while not pq.empty():
            curr_node = pq.get()[1]
            curr_weight = curr_node.get_weight()
            # If the node has not been visited yet
            if curr_node.get_tag() == 0:
                neighbors = self.graph.all_out_edges_of_node(curr_node.get_key())
                for neighbor in neighbors:
                    # edge_weight = self.graph.all_out_edges_of_node(curr_node.get_key()[neighbor])
                    edge_weight = neighbors.get(neighbor)
                    distance = edge_weight
                    nei = self.graph.get_node(neighbor)
                    if curr_weight + distance < nei.get_weight():
                        nei.set_weight(curr_weight + distance)
                        key = str(curr_node.get_key())
                        nei.set_info(curr_node.get_info() + "->" + key)
                        if nei.get_tag() == 0:
                            pq.put((nei.get_tag(), nei))

            curr_node.set_tag(1)  # marked

    def shortest_path_distance(self, id1: int, id2: int) -> float:
        """
        The method returns the shortest distance between two given nodes.
        :param id1: start node.
        :param id2: end (target) node.
        :return: the length of the shortest path between src to dest, if no such path --> returns -1.
        """
        # Checks if both of the keys exist in the graph
        if id1 not in self.graph.get_all_v().keys() or id2 not in self.graph.get_all_v().keys():
            return -1

        # Checks if both of the keys are equal
        if id1 == id2:
            return 0

        source = NodeData(id1)
        destination = self.graph.get_node(id2)
        infinity = float('inf')

        # Calls dijkstra function
        self.dijkstra(id1)

        # returns the tag of the destination only if its distance is lower than infinity
        if destination.get_weight() < infinity:
            return destination.get_weight()
        else:
            return -1

    @staticmethod
    def is_numeric(string):
        """
        The method gets a string and checks if its contains a number
        :param string: a string
        :return: true id the string contains a number
        """
        try:
            int(string)
            return True
        except ValueError:
            return False
