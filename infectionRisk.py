# Import the dictionary of students, teachers and TAs that we imported from excel in the read.py file
import read

# This method is used to calculate the risk that one student has due to his contact with a given class, teacher and TA
# This function will be called for each 
def calculateInfectionRisk(studentRecord, studentID, classList, teacherID, TA_ID):
#def calculateInfectionRisk(studentRecord, studentID, classList):
    filteredInfectedList = []

    for ID in classList:
        if(studentRecord[ID]["givenRisk"] > 0.0 and ID != studentID):
            filteredInfectedList.append(studentRecord[ID]["givenRisk"])
    
    # The class size is the total number of students + 1 teacher + 1 TA
    classSize = len(classList) + 2
    # If there is no TA in the class, the class size will be one smaller
    if(TA_ID == None): 
        classSize -= 1

    for fraction in filteredInfectedList:
        studentRecord[studentID]["givenRisk"] += fraction*(3.0/classSize)

    studentRecord[studentID]["givenRisk"] += read.teachers[teacherID]["givenRisk"]*(3.0/classSize)
    
    if(TA_ID != None):
        studentRecord[studentID]["givenRisk"] += read.tas[TA_ID]["givenRisk"]*(3.0/classSize)

    if(studentRecord[studentID]["healthFlag"] == 1):
        studentRecord[studentID]["givenRisk"] *= 1.7
        
    if(studentRecord[studentID]["Grade"] == 12):
        studentRecord[studentID]["givenRisk"] *= 1.75
    elif(studentRecord[studentID]["Grade"] == 11):
        studentRecord[studentID]["givenRisk"] *= 1.5
    elif(studentRecord[studentID]["Grade"] == 10):
        studentRecord[studentID]["givenRisk"] *= 1.25
    return(studentRecord)

# SAMPLE DATA FOR TESTING
print(calculateInfectionRisk(read.studentRecord, 1, [1, 86, 131, 531], 1, 1))