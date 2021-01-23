# Referenced used to help create object class for a directed graph structure
### reference: https://www.bogotobogo.com/python/python_graph_data_structures.php

class Node:
    def __init__(self,_id):
        self.id = _id
        self.adj = dict()

    def add_weighted_edge(self, _id, info):
        if _id in self.adj:
            self.adj[_id].append(info)
        else:
            self.adj[_id] = list([info]) 

    def get_id(self):
        return "id: {_id}".format(_id = self.id)

    def get_adj(self):
        return self.adj.keys()

    def print_adj(self):
        output = ""
        for key,value in self.adj.items():
            output += "key: {_id:10s} \t weight:{weight} \n\t ".format(_id = key, weight = value)
        return output
    


class Graph:
    def __init__(self, numNode):
        self.N = numNode
        self.graph = dict()
    
    def add_vertex(self, node):
        self.N += 1
        self.graph[node] = Node(node)

    # Only adding the head to the edge of the tailnode since this is a directed graph. Adding the edge to the opposite node will indicate a bi-directional graph 

    # @param tail is the id of a node 
    # @param head is the id of a node
    # @param info a list of infomration corresponding to the edge (i.e [studedntID, chance%])
    def add_edge(self, tail, head, info):
        if tail not in self.graph:
            self.add_vertex(tail)

        if head not in self.graph:
            self.add_vertex(head)
   
        self.graph[tail].add_weighted_edge(head, info)

    def print_graph(self):
        for key,value in self.graph.items():
            print("Node:",key, "\n\t",value.print_adj())

if __name__ == '__main__':
    g = Graph(5)

    g.add_edge("Function A", "Physics B", [1,0.4])

    g.add_edge("Function A", "Bio A", [2, 0.3])

    g.add_edge("Bio A", "Physics B", [3,0.7])

    g.add_edge("Function A", "Physics B", [4,0.9])

    g.add_edge("Physics B", "Chemistry B", [5,0.9])

    g.print_graph()
    

    
    


