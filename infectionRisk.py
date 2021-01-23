# will need to adjust for the fact that multiple possible infectors could be sitting in a classroom, could be travelling to the classroom



# Calculating Percent of Risk Going Forward
# I think This needs to be recalculated at each stage 
def calculateInfectionRisk(checkedStudent, classList):
    
    filteredInfectedList = [chance for chance in classList if chance > 0]

    for student in filteredInfectedList:
        givenRisk += student.infectorChance*(3.0/len(classList))

    if(checkedStudent.healthFlag == 1):
        givenRisk *= 1.7
        
    if(checkedStudent.grade == 12):
        givenRisk *= 1.75
    elif(checkedStudent.grade == 11):
        givenRisk *= 1.5
    elif(checkedStudent.grade == 10):
        givenRisk *= 1.25
    
    return givenRisk


# SAMPLE DATA FOR TESTING
# WILL NEED TO BE REPLACED BY REAL STUDENT DATA AFTER
healthFlag = 1
grade = 9
print(calculateInfectionRisk(0.5, 30))