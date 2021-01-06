import json
from typing import List
from DiGraph import DiGraph
from NodeData import NodeData
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph = DiGraph()

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
        except IOError as exception:
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
            with open(file_name, "w") as write_file:
                json_graph = {"Nodes": [], "Edges": []}
                # save edges as json
                for id1 in self.graph.Neighbors_out.keys():
                    for id2, w in self.all_out_edges_of_node(id1).items():
                        json_graph["Edges"].append({"src": id1, "weight": w, "dest": id2})
                # save nodes as json
                for n in self.graph.nodes.values():
                    if n.pos is None:
                        json_graph["Nodes"].append({"id": n.key})
                    else:
                        json_graph["Nodes"].append({"pos": n.pos, "id": n.key})
            json.dump(json_graph, indent=4, fp=write_file)
            return True
        except IOError as e:
            print(e)
            return False
        finally:
            write_file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        raise NotImplementedError

    """
    def get_transpose(self):
        reverse_graph = DiGraph()
        for key in self.graph.get_all_v().keys():
            reverse_graph.add_node(key)
        for src in reverse_graph.get_all_v().keys():
            for dest, weight in self.graph.all_out_edges_of_node(src):
                reverse_graph.add_edge(src, dest, weight)
        return reverse_graph
        """

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
            # If there is a path between 1d1 to key and also to the opposite direction
            if id1 != key and self.shortest_path(id1, key) != (float('inf'), []) and\
                    self.shortest_path(key, id1) != (float('inf'), []):
                ssc.append(key)
                NodeData(key).set_tag = 1
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
        # Resets all the tags to zero
        for key in self.graph.get_all_v().keys():
            NodeData(key).set_tag = 0
        all_scc = []
        # Go over all the key's nodes in the graph
        for key in self.graph.get_all_v().keys():
            if NodeData(key).get_tag != 1:
                all_scc.append(scc_key)
                scc_key = self.connected_component(key)
        return all_scc

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
