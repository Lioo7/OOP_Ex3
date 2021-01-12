import copy
import math
from collections import deque
import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import json
from datetime import datetime
import time
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx

# from GraphAttributes import Node
from types import SimpleNamespace


def net2(file_name):
    try:
        with open(file_name, "r")as file:
            graph_dict = json.load(file)
            nodes = graph_dict.get("Nodes")
            edges = graph_dict.get("Edges")
            return nodes, edges
    except IOError as e:
        print(e)


if __name__ == '__main__':
    nx_results = []  # contains the results(time) of networkx program
    python_results = []  # contains the results(time) of our python program

    # ==============================================Graph-builder=======================================================

    ga = GraphAlgo()
    graphs = ["G_10_80_1.json", "G_100_800_1.json", "G_1000_8000_1.json", "G_10000_80000_1.json",
              "G_20000_160000_1.json", "G_30000_240000_1.json"]
    paths = [(0, 9), (1, 99), (1, 999), (1, 9000), (1, 18000), (1, 29979)]
    for number in range(6):
        file_name = graphs[number]
        ga.load_from_json(file_name)
        print("graph" + str(file_name))
        dicts = net2(file_name)
        nodes = dicts[0]
        edges = dicts[1]
        graph = nx.DiGraph()
        for currentNode in nodes:
            id = currentNode.get('id')
            # print(id)
            graph.add_node(graph)  # graph or id ???
        for e in edges:
            src = e.get('src')
            dest = e.get('dest')
            w = e.get('w')
            graph.add_edge(src, dest, weight=w)

        # =================================================Networkx-test========================================================

        start = time.time()
        src = paths[number][0]
        dest = paths[number][1]
        path = nx.dijkstra_path(graph, source=src, target=dest, weight='weight')
        end = time.time()
        result = end - start
        print("networkx time")
        print("shortest " + " time from " + str(src) + " to " + str(dest) + " is: " + str(result))
        nx_results.append(result)
        start = time.time()
        strong = nx.strongly_connected_components(graph)
        end = time.time()
        result = end - start
        print("component time   is: " + str(result))
        nx_results.append(result)

        # ==================================================Python-test=========================================================

        start = time.time()
        src = paths[number][0]
        dest = paths[number][1]
        ga.shortest_path(src, dest)
        end = time.time()
        result = end - start
        print("GA time:")
        print("shortest " + " time from " + str(src) + " to " + str(dest) + " is: " + str(result))
        python_results.append(result)

        start = time.time()
        ccs = ga.connected_components()
        end = time.time()
        result = end - start
        # print(nx.edges(graph))
        print("component time for Graph   is: " + str(end - start))
        python_results.append(result)

        start = time.time()
        cc = ga.connected_component(0)
        end = time.time()
        result = end - start
        # print(nx.edges(graph))
        print("component time for id 0   is: " + str(result))
        python_results.append(result)
        print(" ")
        print(" ")
