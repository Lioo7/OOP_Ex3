# OOP_Ex3
## Ex3 : directed & Weighted Graphs - python
**In this project we implemented a weighted directed graph accompanied by different graphs algorithms in Python.<br/>
We used two interfaces to implement the graph properties and we implemented the graph by three classes.<br/>**
## Data Structures:
### NodeData:<br/>
This class represents the set of operations applicable on a node in an directed weighted graph.<br/>
Each node has a unique key plus four additional node fields (weight, position , tag and information) that were used only during the algorithms.<br/>
### DiGraph:<br/>
*The GraphInterface interface is implemented in DiGraph class:*<br/>
This class represents an directional weighted graph.<br/>
It supports a large number of nodes.<br/>
The nodes and the edges are implemented in a data structure – Dictionary.<br/>
There are functions for adding / removing nodes and edges, getting the node data by his key,<br/>
obtaining the amount of nodes / edges there are in the graph, obtaining dictionary of all the nodes in the graph,<br/>
obtaining dictionary of all the nodes connected to (into) node_id,obtaining dictionary of all the nodes connected from node_id,<br/>
obtaining the amount of actions done on the graph (saved as mc).<br/>
### GraphAlgo:<br/>
*The GraphAlgoInterface interface is implemented in GraphAlgo class:*<br/>
The Graph_Algo object contains a graph to activate the algorithms on.<br/>

**This class represents the Graph Theory algorithms including:**<br/>
1.**__init__:** Init this set of algorithms on a given graph<br/>
2.**get_graph:** Return the underlying graph of which this class works<br/>
3.**shortest_path:** Returns the shortest path from node id1 to node id2.<br/>
4.**connected_component:** Finds the Strongly Connected Component(SCC) that node id1 is a part of.<br/>
5.**connected_components:** Finds all the Strongly Connected Component(SCC) in the graph.<br/>
6.**save_to_json:** Saves this weighted directed graph to the given file name - in JSON format.<br/>
7.**load_from_json:** Loads the graph from the file.<br/>
8.**plot_graph:** Plots the graph.<br/>
9.**clear:** PClears the graph  and initializes all the nodes in the graph to their default values.<br/>
10.**dijkstra:** Algorithm for finding the shortest paths between nodes in a graph.<br/>
11.**shortest_path_distance:** Returns the shortest distance between two given nodes.<br/>
12.**is_numeric:** The method gets a string and checks if its contains a number.<br/>




