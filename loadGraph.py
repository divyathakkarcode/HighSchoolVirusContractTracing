import read
import graph

def addEdgeBetweenPeriods(graph, classInfo, tailName, headName, tailPeriod, headPeriod):

    # Iterating between two dictionaries simultaneously, tail node and head node
    # Reference: https://stackoverflow.com/questions/20736709/how-to-iterate-over-two-dictionaries-at-once-and-get-a-result-using-values-and-k

    for (tail_k, tail_v), (head_k, head_v) in zip(classInfo[tailName].items(), classInfo[headName].items()):
        tailStr = "("+tail_k + ") - " + tailPeriod
        headStr = "("+ head_k + ") - " + headPeriod

        

        # Checking the same students of id that belong in period 1 and in period 2 between 2 classes, making note of which class the students have transitioned to (getting the INTERSECTION). 
        # Reference: https://stackoverflow.com/questions/740287/how-to-check-if-one-of-the-following-items-is-in-a-list
        
        students_switching_class =  [_id for _id in tail_v if _id in head_v]
        
        graph.add_edge(tailStr, headStr, students_switching_class)
    


def loadGraph():
    NUM_NODES = 20*4 + 4 #(20 classes * 4 periods + 4 clubs)
    
    g = graph.Graph(NUM_NODES)

    classInfo = read.putStudentsInClass()

    addEdgeBetweenPeriods(g, classInfo, 'ClassP1', 'ClassP2', 'P1', 'P2')

    addEdgeBetweenPeriods(g, classInfo, 'ClassP2', 'ClassP3', 'P2', 'P3')
    
    addEdgeBetweenPeriods(g, classInfo, 'ClassP3', 'ClassP4', 'P3', 'P4')

    
    g.print_graph()

loadGraph()
