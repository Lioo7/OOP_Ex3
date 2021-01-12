import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# def networkx():
#     g = nx.DiGraph()
#     g.add_node(1)
#     g.add_nodes_from(range(2, 7))
#     g.add_weighted_edges_from([(1, 2, 5.5), (2, 3, 4.8), (2, 5, 1), (3, 4, 10.1), (4, 5, 20), (5, 1, 1)])
#     print(nx.shortest_path(g, 1, 5))
#     print(nx.shortest_path_length(g, 1, 5))
#
#     # print(nx.connected_components(g))
#     g = nx.draw(g)
#     plt.show()


def plot_bar_chart():
    """
    based on:
    https://stackoverflow.com/questions/10369681/how-to-plot-bar-graphs-with-same-x-coordinates-side-by-side-dodged
    :return: a bar chart
    """
    # Numbers of pairs of bars you want
    N = 3
    # Font size
    fontsize = 6.5

    # ===================================================plot 1=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10, 5))

    # Width of a bar
    width = 0.3

    plt.subplot(2, 3, 1)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #1: |V|=10, |E|=80')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 2=========================================================
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    plt.subplot(2, 3, 2)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #2: |V|=100, |E|=800')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 3=========================================================
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    plt.subplot(2, 3, 3)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #3: |V|=1,000, |E|=8,000')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 4=========================================================
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    plt.subplot(2, 3, 4)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #4: |V|=10,000, |E|=80,000')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 5=========================================================
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    plt.subplot(2, 3, 5)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #5: |V|=20,000, |E|=160,000')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    # ===================================================plot 6=========================================================
    # Specify the values of blue bars (height)
    python_bar = (23, 25, 17)
    # Specify the values of orange bars (height)
    java_bar = (19, 18, 14)
    # Specify the values of black bars (height)
    networkx_bar = (1, 2, 3)

    plt.subplot(2, 3, 6)
    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + 2 * width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5*fontsize)
    plt.title('Graph #6: |V|=30,000, |E|=2,400,000')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Connected component', 'Connected components', 'Shortest path'), fontsize=fontsize)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ==================================================================================================================
    plt.suptitle('Performance Comparison', fontsize=3*fontsize)
    plt.show()


if __name__ == '__main__':
    # networkx()
    plot_bar_chart()
