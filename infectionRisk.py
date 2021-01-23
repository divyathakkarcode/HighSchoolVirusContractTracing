import read

# Calculating Percent of Risk Going Forward
# I think This needs to be recalculated at each stage 
def calculateInfectionRisk(studentRecord, studentID, classList, teacherID, TA_LastName):
#def calculateInfectionRisk(studentRecord, studentID, classList):
    filteredInfectedList = []
    
    for ID in classList:
        if(studentRecord[studentID]["givenRisk"] != 0):
            filteredInfectedList.append(studentRecord[studentID]["givenRisk"])

    #ADD SECTION TO CALCULATE ONGOING RISK OF TA AND TEACHER WHO TEACHES THAT CLASS
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    for student in filteredInfectedList:
        studentRecord[studentID]["givenRisk"] += studentRecord[studentID]["givenRisk"]*(3.0/len(classList))

    if(studentRecord[studentID]["healthFlag"] == 1):
        studentRecord[studentID]["givenRisk"] *= 1.7
        
    if(studentRecord[studentID]["Grade"] == 12):
        studentRecord[studentID]["givenRisk"] *= 1.75
    elif(studentRecord[studentID]["Grade"] == 11):
        studentRecord[studentID]["givenRisk"] *= 1.5
    elif(studentRecord[studentID]["Grade"] == 10):
        studentRecord[studentID]["givenRisk"] *= 1.25
    return(studentRecord[studentID]["givenRisk"])

# SAMPLE DATA FOR TESTING
print(calculateInfectionRisk(read.studentList(), 1, [1, 8, 40, 49, 63, 81, 92, 150, 158, 207, 247, 266, 311, 327, 340, 351, 397, 418, 460, 487, 492, 512, 526, 539, 541, 571, 574]))