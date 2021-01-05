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
         Test adding a new node to the graph
         Expected node 1 to be in nodes.keys
         """
        self.g.add_node(1)
        print("\nFirst test: self.g.add_node(1)")
        print("Nodes:", self.g.nodes)
        self.assertTrue(1 in self.g.nodes.keys())

        """
        Test adding a new node that already exist
        Expected nodes size remain the same
         """
        self.g.add_node(1)
        print("\nSecond test: self.g.add_node(1)")
        print("Nodes:", self.g.nodes)
        self.assertEqual(1, self.g.v_size())

    def test_remove_node(self):
        """
        Test remove a new node from the graph
        Expected node 1 not to be in nodes.keys
        """
        g = set_small_graph()
        g.remove_node(1)
        print("\nFirst test: self.g.remove_node(1)")
        print("Nodes:", g.nodes)
        self.assertTrue(1 not in g.nodes.keys())

        """
        Test remove a new node that does not exist
        Expected nodes size remain the same
        """
        g.remove_node(1)
        print("\nSecond test: self.g.remove_node(1)")
        print("Nodes:", g.nodes)
        self.assertEqual(2, g.v_size())



    def test_add_edge(self):
        """
        Test adding a new edge to the graph
        Expected edges size increase by 1
        """
        g = set_small_graph()
        g.add_edge(1, 2, 5.5)
        print("First test: g.add_edge(1, 2, 5.5)")
        print("Edges OUT: ", g.Neighbors_out)
        print("Edges IN: ", g.Neighbors_in)
        self.assertEqual(1, g.count_edges)

        """
        Test adding a new edge that already exist
        Expected edges size remain the same
        """
        g.add_edge(1, 2, 10)
        print("\nSecond test: g.add_edge(1, 2, 5.5)")
        print("Edges OUT:", g.Neighbors_out)
        print("Edges IN:", g.Neighbors_in)
        self.assertEqual(1, g.count_edges)

        """
        Test adding a new edge with a negative weight
        Expected edges size remain the same
        """
        g.add_edge(1, 2, -4)
        print("\nThird test: g.add_edge(1, 2, -4)")
        print("Edges OUT:", g.Neighbors_out)
        print("Edges IN:", g.Neighbors_in)
        self.assertEqual(1, g.count_edges)

        """
        Test adding a new edge with a node that does not exist in the graph 
        Expected edges size remain the same
        """
        g.add_edge(1, 10, 9)
        print("\nForth test: g.add_edge(1, 10, 9)")
        print("Edges OUT:", g.Neighbors_out)
        print("Edges IN:", g.Neighbors_in)
        self.assertEqual(1, g.count_edges)


if __name__ == '__main__':
    unittest.main()
