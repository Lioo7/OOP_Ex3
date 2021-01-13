import heapq
import itertools
import json
import math
from typing import List

from numpy.ma.bench import yl

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
            print("Exception: ", e)
            return False
        finally:
            write_file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        More info:
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        keys = self.graph.get_all_v().keys()
        if id1 not in keys or id2 not in keys:
            return float('inf'), []

        if id1 == id2:
            return 0, []

        return self.dijkstra(id1, id2)

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        if id1 not in self.graph.nodes:
            return []

        scc = self.bfs(id1)
        scc = scc & (self.bfs(id1, in_edges=False))
        return list(scc)

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        # If the graph is None, return an empty list []
        """
                Finds all the Strongly Connected Component(SCC) in the graph.
                @return: The list all SCC
                Notes:
                If the graph is None the function should return an empty list []
                """
        # If the graph is None, return an empty list []
        if self.graph is None:
            return []
        flat_covered = []
        all_scc = []
        # Go over all the key's nodes in the graph
        for key in self.graph.get_all_v().keys():
            # the key is not in a scc yet
            if key not in flat_covered:
                scc_key = self.connected_component(key)
                all_scc.append(scc_key)
                flat_covered = list(itertools.chain(*all_scc))
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

    def dijkstra(self, src: int, dest: int) -> (float, list):
        self.clear()
        prev = {src: -1}
        # """saves for each node the previous node"""
        dist = {i: math.inf for i in self.graph.get_all_v().keys()}
        """up date the dist"""
        dist[src] = 0
        self.graph.get_node(src).set_tag(0)
        q = []
        heapq.heappush(q, (0, src))
        """saves for each node his min weight"""
        while q:
            v = heapq.heappop(q)[1]
            for ni, w in self.graph.all_out_edges_of_node(v).items():
                if dist[ni] > dist[v] + w:
                    dist[ni] = dist[v] + w
                    prev[ni] = v
                    heapq.heappush(q, (dist[ni], ni))
                    """push to the queue the new distance and the node_key"""
            if v == dest:
                break

        if dist[dest] == math.inf:
            """there is no path"""
            return float('inf'), []
        path = []
        p = dest

        while p != -1:
            path.insert(0, p)
            p = prev[p]
        return dist[dest], path

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

    def bfs(self, src: int, in_edges: bool = True) -> set:
        nodes_q = [src]
        covered = {src}
        while nodes_q:
            node = nodes_q.pop()
            if in_edges:
                node_nei = self.graph.all_out_edges_of_node(node).keys()
            else:
                node_nei = self.graph.all_in_edges_of_node(node).keys()

            for adj_node in node_nei:
                if adj_node not in covered:
                    covered.add(adj_node)
                    nodes_q.append(adj_node)
        return covered

    def __eq__(self, other):
        return self.__graph == other.__graph
