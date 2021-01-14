import json
import networkx as nx
import time
from Plot import plot_bar_chart
from GraphAlgo import GraphAlgo
from random import uniform


def run_simulation():
    nx_results = []  # contains the result (in sec) of all the functions in networkx (Short|Component|Components)
    py_results = []  # contains the result (in sec) of all the functions in python (Short|Component|Components)
    # contains the result (in sec) of all the functions in java (Short|Component|Components)
    java_results = [0.0024046, 0.0020393, 0.0286995, 0.3990609, 0.5003517, 0.2987889,
                    0.0001906, 0.000615, 0.0005584, 0.0255793, 0.0330737, 0.0009482,
                    0.0001255, 0.00016747, 0.0255405, 0.2244528, 0.757112, 0.9485512]

    """-------------------- Shortest_path comparison --------------------"""

    json_graph = ['../data/G_10_80_1.json', '../data/G_100_800_1.json', '../data/G_1000_8000_1.json',
                  '../data/G_10000_80000_1.json', '../data/G_20000_160000_1.json',
                  '../data/G_30000_240000_1.json']
    i = 1
    for f in json_graph:
        print('----- test', i, ': Shortest_path comparison -----')
        i = i + 1
        graph_nx = compare_nx.load_from_json(f)
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(f)

        time_start = time.time()
        src = int(uniform(0, graph_algo.graph.v_size()))
        dest = int(uniform(0, graph_algo.graph.v_size()))
        list_nx = nx.shortest_path(graph_nx, src, dest, weight='weight')
        time_end = time.time()
        delta = time_end - time_start
        nx_results.append(delta)
        print('Time_nx:', delta)
        print('graph_nx: ', list_nx)

        time_start = time.time()
        graph_algo.shortest_path(src, dest)
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
        random = int(uniform(0, graph_algo.graph.v_size()))
        component_list = graph_algo.connected_component(random)
        time_end = time.time()
        delta = time_end - time_start
        py_results.append(delta)
        # print("component_list:", component_list)
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

    print('----- results -----')
    print("nx_results:", nx_results)
    print("py_results:", py_results)
    print("java_results:", java_results)

    return nx_results, py_results, java_results


class compare_nx:
    """--------------------- Graph-builder ---------------------"""

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

    nx_results_total = 18 * [0]  # contains the result(in sec) of all the funcs in networkx(Short|Component|Components)
    py_results_total = 18 * [0]  # contains the result(in sec) of all the funcs in python(Short|Component|Components)
    java_results_total = 18 * [0]  # contains the result(in sec) of all the funcs in java(Short|Component|Components)

    iterations = 3
    for current_iteration in range(1, iterations + 1):
        print("-------------------iteration number", current_iteration, "----------------------")
        temp = run_simulation()
        # calculates the sum of results so far
        for i in range(0, 18):
            nx_results_total[i] = (nx_results_total[i] + temp[0][i])
            py_results_total[i] = (py_results_total[i] + temp[1][i])
            java_results_total[i] = (java_results_total[i] + temp[2][i])

    # calculates the average of results after all the iterations
    nx_results_avg = []  # contains the result (in sec) of all the functions in networkx (Short|Component|Components)
    py_results_avg = []  # contains the result (in sec) of all the functions in python (Short|Component|Components)
    java_results_avg = []  # contains the result (in sec) of all the functions in java (Short|Component|Components)

    for i in range(0, 18):
        nx_avg = nx_results_total[i] / iterations
        py_avg = py_results_total[i] / iterations
        java_avg = java_results_total[i] / iterations

        nx_results_avg.append(nx_avg)
        py_results_avg.append(py_avg)
        java_results_avg.append(java_avg)

    # Plotting the results in a bar chart
    plot_bar_chart(nx_results_avg, py_results_avg, java_results_avg)
