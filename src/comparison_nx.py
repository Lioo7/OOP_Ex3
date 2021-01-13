import json
import networkx as nx
import time

from GraphAlgo import GraphAlgo


class compare_nx:
    """-------------------- Graph-builder --------------------"""
    @staticmethod
    def load_from_json(filename: str):
        gr = nx.DiGraph()
        try:
            with open(filename, "r") as read_file:
                dict_graph = json.load(read_file)
                for dic in dict_graph["Nodes"]:
                    gr.add_node(dic["id"])
                for dic in dict_graph["Edges"]:
                    gr.add_edge(dic["src"], dic["dest"], weight=dic["w"])
        except IOError as e:
            print(e)
        return gr


if __name__ == '__main__':
    nx_results = []  # contains the result (in sec) of all the functions in networkx (Short|Component|Components)
    py_results = []  # contains the result (in sec) of all the functions in python (Short|Component|Components)

    """-------------------- Shortest_path comparison --------------------"""

    json_graph = ['../data/G_10_80_1.json', '../data/G_100_800_1.json', '../data/G_1000_8000_1.json',
                  '../data/G_10000_80000_1.json', '../data/G_20000_160000_1.json', '../data/G_30000_240000_1.json']
    i = 1
    for f in json_graph:
        print('----- test', i, ': Shortest_path comparison -----')
        i = i + 1
        graph_nx = compare_nx.load_from_json(f)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(f)

        time_start = time.time()
        list_nx = nx.shortest_path(graph_nx, 1, 5, weight='weight')
        time_end = time.time()
        delta = time_end - time_start
        nx_results.append(delta)
        print('Time_nx:', delta)
        print('graph_nx: ', list_nx)

        time_start = time.time()
        graph_algo.shortest_path(1, 5)
        time_end = time.time()
        delta = time_end - time_start
        py_results.append(delta)
        print('Time_python:', delta)
        print('graph_algo:', graph_algo.shortest_path(1, 5), '\n')

    """-------------------- Connected_component comparison --------------------"""

    i = 1
    for f in json_graph:
        print('----- test', i, ': Connected_component (Id_scc) -----')
        i = i + 1
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(f)

        time_start = time.time()
        graph_algo.connected_component(3)
        time_end = time.time()
        delta = time_end - time_start
        py_results.append(delta)
        print('Time_python:', delta, '\n')

        nx_results.append(0)  # Connected_component does not exist in nx -> always zero

    """-------------------- Connected_components comparison --------------------"""


    i = 1
    for f in json_graph:
        print('----- test', i, ': Connected_componentS (ALL_scc) -----')
        i = i + 1
        graph_nx = compare_nx.load_from_json(f)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(f)

        time_start = time.time()
        list_nx = nx.kosaraju_strongly_connected_components(graph_nx)
        time_end = time.time()
        delta = time_end - time_start
        nx_results.append(delta)
        print('Time_nx:', delta)

        time_start = time.time()
        graph_algo.connected_components()
        time_end = time.time()
        delta = time_end - time_start
        py_results.append(delta)
        print('Time_python:', delta, '\n')
