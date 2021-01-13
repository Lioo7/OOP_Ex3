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

    def test_load_and_save(self):
        file = '../data/test_save.json'
        self.graph_algo.save_to_json(file)
        self.g1 = GraphAlgo()
        self.assertTrue(self.g1.load_from_json(file))
        print(self.g1.get_graph())

        self.g2 = GraphAlgo()
        self.assertTrue(self.g2.load_from_json('../data/A5'))
        print(self.g2.get_graph())

        self.g3 = GraphAlgo()
        self.assertTrue(self.g3.load_from_json('../data/G_100_800_1.json'))
        print(self.g3.get_graph())

    def test_shortest_path(self):
        self.assertIsNotNone(self.graph_algo.shortest_path(1, 2))
        self.assertIsNotNone(self.graph_algo.shortest_path(5, 6))
        self.assertEqual((3.5, [1, 2, 4]), self.graph_algo.shortest_path(1, 4))
        self.assertEqual((3, [9, 10]), self.graph_algo.shortest_path(9, 10))
        self.assertEqual((float('inf'), []), self.graph_algo.shortest_path(1, 10))
        self.assertEqual((float('inf'), []), self.graph_algo.shortest_path(-2, 1))
        self.assertEqual((0, []), self.graph_algo.shortest_path(7, 7))
        self.assertEqual((float('inf'), []), self.graph_algo.shortest_path(1, 11))
        self.assertEqual((float('inf'), []), self.graph_algo.shortest_path(0, -5))
        self.graph.add_edge(4, 6, 1)
        self.graph.add_edge(8, 9, 2)
        self.graph.add_edge(8, 10, 8)
        self.assertEqual((13.1, [4, 6, 8, 9, 10]), self.graph_algo.shortest_path(4, 10))
        self.graph.remove_edge(8, 9)
        self.assertEqual((16.1, [4, 6, 8, 10]), self.graph_algo.shortest_path(4, 10))
        self.assertEqual((20.6, [1, 2, 4, 6, 8, 5]), self.graph_algo.shortest_path(1, 5))
        self.graph.add_edge(3, 5, 15)
        self.assertEqual((18, [1, 3, 5]), self.graph_algo.shortest_path(1, 5))

    def test_connected_component(self):
        self.assertEqual([1, 2, 3, 4], self.graph_algo.connected_component(1))
        self.assertEqual([1, 2, 3, 4], self.graph_algo.connected_component(4))
        self.assertEqual([8, 5, 6], self.graph_algo.connected_component(5))
        self.assertEqual([7], self.graph_algo.connected_component(7))
        self.assertEqual([9, 10], self.graph_algo.connected_component(9))
        self.graph.add_edge(4, 6, 2)
        self.graph.add_edge(5, 3, 1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 8], self.graph_algo.connected_component(1))
        self.graph.add_edge(9, 7, 1)
        self.graph.add_edge(7, 10, 5)
        self.assertEqual([9, 10, 7], self.graph_algo.connected_component(10))
        self.graph.remove_edge(1, 2)
        self.graph.remove_edge(1, 3)
        self.assertEqual([1], self.graph_algo.connected_component(1))
        self.assertEqual([2, 3, 4, 5, 6, 8], self.graph_algo.connected_component(6))

    def test_connected_components(self):
        self.assertIsNotNone(self.graph_algo.connected_components())
        self.assertEqual([[1, 2, 3, 4], [8, 5, 6], [7], [9, 10]], self.graph_algo.connected_components())
        self.graph.remove_edge(1, 3)
        self.graph.remove_edge(1, 2)
        self.assertEqual([[1], [2, 3, 4], [8, 5, 6], [7], [9, 10]], self.graph_algo.connected_components())
        self.graph.add_edge(1, 7, 3)
        self.graph.add_edge(7, 1, 5)
        self.assertEqual([[1, 7], [2, 3, 4], [8, 5, 6], [9, 10]], self.graph_algo.connected_components())
        self.graph.remove_edge(9, 10)
        self.assertEqual([[1, 7], [2, 3, 4], [8, 5, 6], [9], [10]], self.graph_algo.connected_components())
        self.assertEqual(5, len(self.graph_algo.connected_components()))

    def test_plot_graph(self):
        self.graph_algo.load_from_json('../data/G_100_800_1.json')
        self.graph_algo.plot_graph()

    def test_is_numeric(self):
        self.assertTrue(self.graph_algo.is_numeric("1"))
        self.assertFalse(self.graph_algo.is_numeric("f"))


if __name__ == '__main__':
    unittest.main()
