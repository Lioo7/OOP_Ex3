import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = DiGraph()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_node(5)
        self.graph.add_node(6)
        self.graph.add_node(7)
        self.graph.add_node(8)
        self.graph.add_node(9)
        self.graph.add_node(10)
        self.graph.add_edge(1, 2, 1.5)
        self.graph.add_edge(1, 3, 3)
        self.graph.add_edge(2, 4, 2)
        self.graph.add_edge(3, 2, 4.3)
        self.graph.add_edge(4, 3, 9)
        self.graph.add_edge(4, 1, 5)
        self.graph.add_edge(5, 6, 3)
        self.graph.add_edge(6, 8, 7.1)
        self.graph.add_edge(8, 5, 9)
        self.graph.add_edge(9, 10, 3)
        self.graph.add_edge(10, 9, 5.8)
        self.graph_algo = GraphAlgo(self.graph)

    def test_get_graph(self):
        self.assertIsNotNone(self.graph_algo.get_graph())
        self.assertEqual(self.graph, self.graph_algo.get_graph())
        self.g = DiGraph()
        self.ga = GraphAlgo(self.g)
        self.assertEqual(0, self.ga.get_graph().v_size())
        self.assertEqual(0, self.ga.get_graph().e_size())
        self.assertEqual(0, self.ga.get_graph().get_mc())
        self.g.add_node(1)
        self.g.add_node(2)
        self.assertEqual(2, self.ga.get_graph().v_size())
        self.g.add_edge(1, 2, 4)
        self.assertEqual(1, self.ga.get_graph().e_size())

    def test_shortest_path(self):
        self.assertIsNotNone(self.graph_algo.shortest_path(1, 2))
        self.assertIsNotNone(self.graph_algo.shortest_path(5, 6))

    def test_connected_component(self):
        self.assertEqual([1, 2, 3, 4], self.graph_algo.connected_component(1))
        self.assertEqual([4, 1, 2, 3], self.graph_algo.connected_component(4))
        self.assertEqual([5, 6, 8], self.graph_algo.connected_component(5))
        self.assertEqual([7], self.graph_algo.connected_component(7))
        self.assertEqual([9, 10], self.graph_algo.connected_component(9))
        self.graph.add_edge(4, 6, 2)
        self.graph.add_edge(5, 3, 1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 8], self.graph_algo.connected_component(1))
        self.graph.add_edge(9, 7, 1)
        self.graph.add_edge(7, 10, 5)
        self.assertEqual([10, 7, 9], self.graph_algo.connected_component(10))
        self.graph.remove_edge(1, 2)
        self.graph.remove_edge(1, 3)
        self.assertEqual([1], self.graph_algo.connected_component(1))
        self.assertEqual([6, 2, 3, 4, 5, 8], self.graph_algo.connected_component(6))

    def test_connected_components(self):
        self.assertIsNotNone(self.graph_algo.connected_components())
        self.assertEqual([[1, 2, 3, 4], [5, 6, 8], [7], [9, 10]], self.graph_algo.connected_components())
        self.graph.remove_edge(1, 3)
        self.graph.remove_edge(1, 2)
        self.assertEqual([[1], [2, 3, 4], [5, 6, 8], [7], [9, 10]], self.graph_algo.connected_components())
        self.graph.add_edge(1, 7, 3)
        self.graph.add_edge(7, 1, 5)
        self.assertEqual([[1, 7], [2, 3, 4], [5, 6, 8], [9, 10]], self.graph_algo.connected_components())
        self.graph.remove_edge(9, 10)
        self.assertEqual([[1, 7], [2, 3, 4], [5, 6, 8], [9], [10]], self.graph_algo.connected_components())
        self.assertEqual(5, len(self.graph_algo.connected_components()))


if __name__ == '__main__':
    unittest.main()
