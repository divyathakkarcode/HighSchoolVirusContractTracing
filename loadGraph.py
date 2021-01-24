import read
import graph
import infectionRisk

def addEdgeBetweenPeriods(graph, classInfo, tailName, headName, tailPeriod, headPeriod, studentRecord):

    # Iterating between two dictionaries simultaneously, tail node and head node
    # Reference: https://stackoverflow.com/questions/20736709/how-to-iterate-over-two-dictionaries-at-once-and-get-a-result-using-values-and-k

    for (tail_k, tail_v), (head_k, head_v) in zip(classInfo[tailName].items(), classInfo[headName].items()):
        # varName_k is a str of the class name (i.e Functions A)
        # varName_v is a list of [ [list of student ids], teacherID, teachingAssistantID)
        
        tailStr = "("+ tail_k + ") - " + tailPeriod
        headStr = "("+ head_k + ") - " + headPeriod
        
        
        # Since some of the TA's dont teach all the courses at a given period, some will not have a TA. So append None as a result
        if len(tail_v)  == 2:
            tail_v.append(None)

        if len(head_v) == 2:
            head_v.append(None)

        # Calculating the infection risk per class as the start of the class 
        for student in tail_v[0]:
            infectionRisk.calculateInfectionRisk(studentRecord, student, tail_v[0], tail_v[1], tail_v[2])

       
        # Checking the same students of id that belong in period 1 and in period 2 between 2 classes, making note of which class the students have transitioned to (getting the INTERSECTION). 
        # Reference: https://stackoverflow.com/questions/740287/how-to-check-if-one-of-the-following-items-is-in-a-list
        students_switching_class =  [[_id, studentRecord[_id]["givenRisk"]] for _id in tail_v[0] if _id in head_v[0]]
        
        graph.add_edge(tailStr, headStr, students_switching_class)
    


def loadGraph():
    NUM_NODES = 20*4 + 11 #(20 classes * 4 periods + 11 clubs)
    
    g = graph.Graph(NUM_NODES)

    # Getting class info,  
    classInfo = read.putStudentsInClass()

    # Getting student record
    studentRecord = read.studentRecord

    # Getting Teacher record
    teacherRecord = read.teachers

    # Getting Teaching Assistant Record
    TARecord = read.tas

    # Adding Edges between periods 1 & 2, and periods 3 & 4
    addEdgeBetweenPeriods(g, classInfo, 'ClassP1', 'ClassP2', 'P1', 'P2', studentRecord)
    addEdgeBetweenPeriods(g, classInfo, 'ClassP3', 'ClassP4', 'P3', 'P4', studentRecord)
    
    g.print_graph()

    # Printing all the students that have a 100% chance of catching the infection
    print("Below is listed the students who are certaintly infected (100%)")
    print("-"*40)
    for student in studentRecord:
        if studentRecord[student]["givenRisk"] == 1:
            print(studentRecord[student]["Name"])
  

    # Printing all the teachers that have a 100% chance of catching the infection
    print("\n\n")
    print("Below is listed the teachers who are certaintly infected (100%)")
    print("-"*40)
    for teacher in teacherRecord:
        if teacherRecord[teacher]["givenRisk"] == 1:
            print(teacherRecord[teacher]["Name"])
    
    print("\n")
    # Printing all the TAs that have a 100% chance of catching the infection
    print("Below is listed the TAs who are certaintly infected (100%)")
    print("-"*40)
    for TA in TARecord:
        if TARecord[TA]["givenRisk"] == 1:
            print(TARecord[TA]["Name"])
    



loadGraph()


