import matplotlib.pyplot as plt
import numpy as np


def plot_bar_chart(nx: dict, py: dict, java: dict):
    """
    based on:
    https://stackoverflow.com/questions/10369681/how-to-plot-bar-graphs-with-same-x-coordinates-side-by-side-dodged
    :return: a bar chart
    """
    # Numbers of pairs of bars you want
    N = 3
    # Font size
    fontsize = 6.7

    # ===================================================plot 1=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[0], nx[0+6], nx[0+12]
    # Specify the values of orange bars (height)
    python_bar = py[0], py[0+6], py[+12]
    # Specify the values of green bars (height)
    java_bar = java[0], java[0+6], java[+12]

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(10, 5))

    # Width of a bar
    width = 0.3

    plt.subplot(2, 3, 1)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize, fontweight='bold')
    plt.title('Graph #1: |V|=10, |E|=80', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 2=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[1], nx[1+6], nx[1+12]
    # Specify the values of orange bars (height)
    python_bar = py[1], py[1+6], py[1+12]
    # Specify the values of green bars (height)
    java_bar = java[1], java[1+6], java[1+12]

    plt.subplot(2, 3, 2)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize, fontweight='bold')
    plt.title('Graph #2: |V|=100, |E|=800', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 3=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[2], nx[2+6], nx[2+12]
    # Specify the values of orange bars (height)
    python_bar = py[2], py[2+6], py[2+12]
    # Specify the values of green bars (height)
    java_bar = java[2], java[2+6], java[2+12]
    plt.subplot(2, 3, 3)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize, fontweight='bold')
    plt.title('Graph #3: |V|=1,000, |E|=8,000', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 4=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[3], nx[3+6], nx[3+12]
    # Specify the values of orange bars (height)
    python_bar = py[3], py[3+6], py[3+12]
    # Specify the values of green bars (height)
    java_bar = java[3], java[3+6], java[3+12]

    plt.subplot(2, 3, 4)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize)
    plt.title('Graph #4: |V|=10,000, |E|=80,000', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ===================================================plot 5=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[4], nx[4+6], nx[4+12]
    # Specify the values of orange bars (height)
    python_bar = py[4], py[4+6], py[4+12]
    # Specify the values of green bars (height)
    java_bar = java[4], java[4+6], java[4+12]

    plt.subplot(2, 3, 5)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize, fontweight='bold')
    plt.title('Graph #5: |V|=20,000, |E|=160,000', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    # ===================================================plot 6=========================================================
    # Data on X-axis
    # Specify the values of blue bars (height)
    networkx_bar = nx[5], nx[5+6], nx[5+12]
    # Specify the values of orange bars (height)
    python_bar = py[5], py[5+6], py[5+12]
    # Specify the values of green bars (height)
    java_bar = java[5], java[5+6], java[5+12]

    plt.subplot(2, 3, 6)
    # Plotting
    plt.bar(ind, networkx_bar, width, label='Networkx')
    plt.bar(ind + width, python_bar, width, label='Python')
    plt.bar(ind + 2 * width, java_bar, width, label='Java')

    # plt.xlabel('Here goes x-axis label')
    plt.ylabel('Run time(in sec)', fontsize=1.5 * fontsize, fontweight='bold')
    plt.title('Graph #6: |V|=30,000, |E|=2,400,000', fontweight='bold')

    # plt.xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, ('Shortest path', 'Connected component', 'Connected components'), fontsize=fontsize, fontweight='bold')

    # Finding the best position for legends and putting it
    plt.legend(loc='best')

    # ==================================================================================================================
    plt.suptitle('Performance Comparison', fontsize=3 * fontsize, fontweight='bold')
    plt.show()


if __name__ == '__main__':
    plot_bar_chart()
