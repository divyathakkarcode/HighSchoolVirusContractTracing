# Import the dictionary of students, teachers and TAs that we imported from excel in the read.py file
import read
import math

# This method is used to calculate the risk that one student has due to his contact with a given class, teacher and TA
# This function will be called for each student at each stage that they risk transfer of infection (switching from P1/P2 or P3/P4 or being in class with other infected people)
def calculateInfectionRisk(studentRecord, studentID, classList, teacherID, TA_ID):
    # This list holds the infection possibilities of those in contact as a fraction
    filteredInfectedList = []

    # We filter out interactions with those of 0% risk and filter out an interaction with yourself as you cannot infect yourself further
    for ID in classList:
        if(studentRecord[ID]["givenRisk"] > 0.0 and ID != studentID):
            filteredInfectedList.append(studentRecord[ID]["givenRisk"])
    
    # The class size is the total number of students + 1 teacher + 1 TA
    classSize = len(classList) + 2
    # If there is no TA in the class, the class size will be one smaller
    if(TA_ID == None): 
        classSize -= 1

    # For each interaction with a possibly infected person, this student's own risk increases
    # The factor of increase is the other interactor's risk factor fraction multiplied by 3/classSize
    # 3/classSize is chosen to multiply as each person is assumed to transmit the virus to 3 people in a single iccubation period
    # so we assume 3 people in the interaction setting could get infected and each of those members from the class size has an equal chance of infection
    for fraction in filteredInfectedList:
        studentRecord[studentID]["givenRisk"] += fraction*(3.0/classSize)

    # Update the risk added from the teacher in that class
    studentRecord[studentID]["givenRisk"] += read.teachers[teacherID]["givenRisk"]*(3.0/classSize)
    
    # Update the risk added from the TA in that class, if there is one
    if(TA_ID != None):
        studentRecord[studentID]["givenRisk"] += read.tas[TA_ID]["givenRisk"]*(3.0/classSize)

    # Increase risk factors accordingly if the student has a health condition
    if(studentRecord[studentID]["healthFlag"] == 1):
        studentRecord[studentID]["givenRisk"] *= 1.7
    
    # Increase risk factors accordingly if the student has a higher age
    if(studentRecord[studentID]["Grade"] == 12):
        studentRecord[studentID]["givenRisk"] *= math.sqrt(1.75)
    elif(studentRecord[studentID]["Grade"] == 11):
        studentRecord[studentID]["givenRisk"] *= math.sqrt(1.5)
    elif(studentRecord[studentID]["Grade"] == 10):
        studentRecord[studentID]["givenRisk"] *= math.sqrt(1.25)
    
    # If the student already has a 100% of infection or greater, cap the value off at 100%
    if(studentRecord[studentID]["givenRisk"]) >= 1:
        studentRecord[studentID]["givenRisk"] = 1

    return(studentRecord)