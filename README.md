# OOP_Ex3
![alt text](https://i.ibb.co/MpFkXKD/LOGO-1.jpg)

## This project was made during our OOP course at Ariel University in the Department of Computer Science, 2021.

### Project site: https://github.com/ElhaiMansbach/OOP_Ex3.git

### Made by: Elhai Mansbach & Lioz Akirav.

**In this project is about implementing data structure and algorithms in a weighted directed graph accompanied by different graphs algorithms in Python.<br/>
We used two interfaces to implement the graph properties and we implemented the graph by three classes.<br/>**

## Illustration :


![](https://miro.medium.com/max/1228/1*OUqMXd2jmLprCqWULLll8w.gif)


## Data Structures:

### NodeData:<br/>
This class represents the set of operations applied to a node in a directed weighted graph.<br/>
Each node has a unique key plus four additional node fields (weight, position, tag, and information) that were used only during the algorithms.<br/>

### DiGraph:<br/>
*The GraphInterface interface is implemented in DiGraph class:*<br/>
This class represents a directional weighted graph.<br/>
It supports over 10^6 vertices, with an average degree of 10.<br/>
The nodes and the edges are implemented in a data structure – Dictionary.<br/>
The class includes these functions:
| function | Description |
| --- | --- |
| v_size |  Returns the number of vertices in this graph |
| e_size | Returns the number of edges in this graph |
| get_all_v | Returns a dictionary of all the nodes in the graph |
| all_in_edges_of_node | Returns a dictionary of all the nodes connected to the given node_id |
| all_out_edges_of_node | Returns a dictionary of all the nodes connected from the given node_id |
| get_mc | Returns the number of changes made in the graph |
| add_edge | Adds an edge to the graph |
| add_node | Adds a node to the graph |
| get_node | Gets a node's key and returns the NodeData |
| remove_node | Removes a node from the graph |
| remove_edge | Removes an edge from the graph |



### GraphAlgo:<br/>
*The GraphAlgoInterface interface is implemented in GraphAlgo class:*<br/>
The Graph_Algo object contains a graph to activate the algorithms on.<br/>

**This class represents the Graph Theory algorithms including these functions:**<br/>
* __init__ - Initialize the graphh<br/>
* get_graph - Returns the underlying graph of which this class works<br/>
* shortest_path - Returns the shortest path and distance from node id1 to node id2.<br/>
* connected_component - Finds the Strongly Connected Component(SCC) that node id1 is a part of.<br/>
* connected_components - Finds all the Strongly Connected Component(SCC) in the graph.<br/>
* save_to_json - Saves this weighted directed graph to the given file name - in JSON format.<br/>
* load_from_json - Loads the graph from the file.<br/>
* plot_graph - Plots the graph.<br/>

**This class also include these private functions:**<br/>
* clear - PClears the graph and initializes all the nodes in the graph to their default values.<br/>
* dijkstra - Algorithm for finding the shortest paths between nodes in a graph.<br/>
* shortest_path_distance - Returns the shortest distance between two given nodes.<br/>
* is_numeric - The method gets a string and checks if its contains a number.<br/>



## Tests:

This ptoject includes two unittest files :
* test_DiGraph - Testing DiGraph class's functions.
* test_GraphAlgo - Testing GraphAlgo class's functions.


 ## Sources ##
 * https://www.softwaretestinghelp.com/dijkstras-algorithm-in-java/
 * https://www.coursera.org/lecture/advanced-data-structures/core-dijkstras-algorithm-2ctyF
 * https://en.wikipedia.org/wiki/Directed_graph

