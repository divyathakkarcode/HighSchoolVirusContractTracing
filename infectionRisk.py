classList = [0.5, 0.4, 0.2, 0, 0, 0.1]
classList = {"Id": 10, }

# Calculating Percent of Risk Going Forward
# I think This needs to be recalculated at each stage 
def calculateInfectionRisk(studentRecord, studentID, classList):
    
    filteredInfectedList = [chance for chance in classList if chance > 0]

    for student in filteredInfectedList:
        studentRecord[studentID]["givenRisk"] += studentRecord[studentID]["givenRisk"]*(3.0/len(classList))

    if(studentRecord[studentID]["healthFlag"] == 1):
        studentRecord[studentID]["givenRisk"] *= 1.7
        
    if(studentRecord[studentID]["grade"] == 12):
        studentRecord[studentID]["givenRisk"] *= 1.75
    elif(studentRecord[studentID]["grade"] == 11):
        studentRecord[studentID]["givenRisk"] *= 1.5
    elif(studentRecord[studentID]["grade"] == 10):
        studentRecord[studentID]["givenRisk"] *= 1.25
    # given Risk for the student has been updated and does not need to be updated


# SAMPLE DATA FOR TESTING
# WILL NEED TO BE REPLACED BY REAL STUDENT DATA AFTER
healthFlag = 1
grade = 9
print(calculateInfectionRisk(0.5, 30))