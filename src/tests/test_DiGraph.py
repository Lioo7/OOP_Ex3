import unittest
from DiGraph import DiGraph
from NodeData import NodeData
from EdgeData import EdgeData
import random

def set_small_graph():
    # Creates a graph with 3 nodes(1-3)
    g = DiGraph()
    for node in range(1, 4):
        g.add_node(node)
    return g


def set_random_graph():
    # Creates a graph with 10 nodes and 10 edges with a random weight
    g = DiGraph()
    for node in range(1, 11):
        g.add_node(node)
    for node in range(1, 10):
        weight = random.randint(1, 11)
        g.add_edge(node, node + 1, weight)
    return g


class TestDiGraph(unittest.TestCase):

    def setUp(self) -> None:
        # Creates an empty graph
        self.g = DiGraph()

    def test_add_node(self):
        """
         # Test adding a new node to the graph
         # Expected node 1 to be in nodes.keys
         """
        self.g.add_node(1)
        print("G NODES: ", self.g.nodes)
        self.assertTrue(1 in self.g.nodes.keys())

        """
        # Test adding a new node which already exist to the graph
        # Expected nodes size remain the same
         """
        self.g.add_node(1)
        print("G NODES: ", self.g.nodes)
        self.assertEqual(1, self.g.v_size())


    def test_add_edge(self):
        """
        # Test adding a new edge to the graph
        # Expected edges size increase by 1
        """
        g = set_small_graph()
        g.add_edge(0, 1, 5.5)
        self.assertEqual(1, g.count_edges)


if __name__ == '__main__':
    unittest.main()
