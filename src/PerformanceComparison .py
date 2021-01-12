import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def networkx():
    g = nx.DiGraph()
    g.add_node(1)
    g.add_nodes_from(range(2, 7))
    g.add_weighted_edges_from([(1, 2, 5.5), (2, 3, 4.8), (2, 5, 1), (3, 4, 10.1), (4, 5, 20), (5, 1, 1)])
    print(nx.shortest_path(g, 1, 5))
    print(nx.shortest_path_length(g, 1, 5))
    # print(nx.connected_components(g))
    g = nx.draw(g)
    plt.show()


def draw_bar_chart():
    """
    based on: https://matplotlib.org/3.3.3/gallery/lines_bars_and_markers/
    barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    :return: a bar chart
    """
    labels = ['CONNECTED COMPONENT', 'CONNECTED COMPONENTS', 'SHORTEST PATH', '4,', '5']
    # plot 1:
    python_means = [20, 34, 30, 35, 27]
    java_means = [20, 32, 34, 20, 25]
    nx_means = [1, 8, 9, 10, 12]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, python_means, width, label='Python')
    rects2 = ax.bar(x + width / 2, java_means, width, label='Java')
    rects3 = ax.bar(x + width / 2, nx_means, width, label='NetworkX')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Run time(in sec)')
    fig.suptitle('Performance Comparison', fontsize=12)
    ax.set_title('Graph #1')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    autolabel(rects1, ax)
    autolabel(rects2, ax)
    autolabel(rects3, ax)

    fig.tight_layout()

    plt.show()


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def draw():
    # Numbers of pairs of bars you want
    N = 3

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

    # Plotting
    plt.bar(ind, python_bar, width, label='Python')
    plt.bar(ind + width, java_bar, width, label='Java')
    plt.bar(ind + width, networkx_bar, width, label='Networkx')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)')
    plt.title('Performance Comparison')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('CONNECTED COMPONENT', 'CONNECTED COMPONENTS', 'SHORTEST PATH'))

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    # networkx()
    # draw_bar_chart()
    draw()
