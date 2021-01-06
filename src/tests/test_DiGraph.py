import unittest
from DiGraph import DiGraph


def set_small_graph():
    # Creates a graph with 3 nodes(1-3)
    g = DiGraph()
    for node in range(1, 4):
        g.add_node(node)
    return g


def set_connected_graph():
    # Creates a graph with 10 nodes and 9 edges
    g = DiGraph()
    for node in range(1, 11):
        g.add_node(node)
    for node in range(1, 10):
        weight = node + (node + 1)
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

    def test_remove_edge(self):
        """
        Test removing an edge from the graph
        Expected edges size increase by 1
        """
        g = set_connected_graph()
        g.remove_edge(1, 2)
        print("First test: g.remove_edge(1, 2)")
        print("Edges OUT: ", g.Neighbors_out)
        print("Edges IN: ", g.Neighbors_in)
        self.assertEqual(8, g.count_edges)

        """
        Test try to remove an edge that does not exist
        Expected edges size remain the same
        """
        g.remove_edge(1, 2)
        print("\nSecond test: g.remove_edge(1, 2)")
        print("Edges OUT:", g.Neighbors_out)
        print("Edges IN:", g.Neighbors_in)
        self.assertEqual(8, g.count_edges)

        """
        Test try to remove an edge with a node that does not exist in the graph
        Expected edges size remain the same
        """
        g.remove_edge(1, 100)
        print("\nForth test: g.remove_edge(1, 100)")
        print("Edges OUT:", g.Neighbors_out)
        print("Edges IN:", g.Neighbors_in)
        self.assertEqual(8, g.count_edges)

    def test_all_in_edges_of_node(self):
        """
        Test returns all the edges that connect to the given node
        Expected: {4: 9}
        """
        g = set_connected_graph()
        expected = {4: 9}
        print("Edges IN: ", g.all_in_edges_of_node(5))
        self.assertEqual(expected, g.all_in_edges_of_node(5))

        """
        Test returns all the edges that connect to the given node that does not exist
        Expected: None
        """
        g = set_connected_graph()
        expected = None
        print("Edges IN: ", g.all_in_edges_of_node(100))
        self.assertEqual(expected, g.all_in_edges_of_node(100))

    def test_all_out_edges_of_node(self):
        """
        Test returns all the edges that go out from the given node
        Expected: {6: 11}
        """
        g = set_connected_graph()
        expected = {6: 11}
        print("Edges OUT: ", g.all_out_edges_of_node(5))
        self.assertEqual(expected, g.all_out_edges_of_node(5))

        """
        Test returns all the edges that connect to the given node that does not exist
        Expected: None
        """
        g = set_connected_graph()
        expected = None
        print("Edges IN: ", g.all_out_edges_of_node(100))
        self.assertEqual(expected, g.all_out_edges_of_node(100))

    def test_v_size(self):
        """
        Test the number of vertices in the graph
        Expected: 1
        """
        self.g.add_node(1)
        print("\nTest: self.g.add_node(1)")
        print("Nodes:", self.g.nodes)
        self.assertTrue(self.g.v_size() == 1)

    def test_e_size(self):
        """
        Test the number of edges in the graph
        Expected: 0
        """
        self.assertTrue(self.g.v_size() == 0)

        """
        Test the number of edges in the graph
        Expected: 2
        """
        self.g.add_node(1)
        self.g.add_node(2)
        self.g.add_edge(1, 2, 55.5)
        self.g.add_edge(2, 1, 77.7)
        self.assertTrue(self.g.v_size() == 2)

    def test_get_mc(self):
        self.g.add_node(1)  # +1
        self.g.add_node(2)  # +1
        self.g.add_node(3)  # +1
        self.g.add_node(3)  # +0
        self.assertEqual(3, self.g.get_mc())
        self.assertEqual(3, self.g.v_size())
        self.g.add_edge(1, 2, 55.5)  # +1
        self.g.add_edge(1, 3, 44.4)  # +1
        self.g.add_edge(2, 1, 77.7)  # +1
        self.g.add_edge(2, 1, 50)  # +0
        self.g.add_edge(2, 3, 33)  # +1
        self.g.add_edge(3, 1, 42)  # +1
        self.assertEqual(8, self.g.get_mc())
        self.assertEqual(3, self.g.v_size())
        self.assertEqual(5, self.g.e_size())
        self.g.remove_edge(2, 3)  # +1
        self.g.remove_node(1)  # +5
        self.assertEqual(14, self.g.get_mc())
        self.assertEqual(2, self.g.v_size())
        self.assertEqual(0, self.g.e_size())


if __name__ == '__main__':
    unittest.main()
