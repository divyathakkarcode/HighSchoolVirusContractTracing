<<<<<<< Updated upstream
from openpyxl import load_workbook 
wb2 = load_workbook('OEC2021-School_Record_Book.xlsx') 
sheet = wb2['ZBY1 Status']
dict = {}
j=0
for i in sheet["A2":"D5"]:
    dict[j] = {"StudentID": i[0].value, "Name": i[2].value+" "+i[1].value, "Infected": 1}
    print(dict[j])
    j+=1
=======
from openpyxl import load_workbook
#loading excel file
wb2 = load_workbook('OEC2021-School_Record_Book.xlsx')

#This class creates a dictonary with all infected students
def infectionList():
    #loading virus 
    sheet = wb2['ZBY1 Status']
    infected = {}
    j=0
    lastRow = sheet.max_row
    for i in sheet["A2":"D"+str(lastRow)]:
        infected[j] = {"StudentID": i[0].value, "Name": i[2].value+" "+i[1].value, "Infected": 1}
        #print(infected[j])
        j+=1
    return infected

#This class creates a dictonary with all teachers
def teacherList():
    sheet = wb2['Teacher Records']
    teachers = {}
    lastRow = sheet.max_row
    for i in sheet["A2":"D"+str(lastRow)]:
        teachers[i[0].value] = {"TeacherNumber": i[0].value, "Name": i[2].value+" "+i[1].value, "Class": i[3].value}
        #print(teachers[i[0].value])
    return teachers

#This class creates a dictonary with all teaching assistants
def TAList():
    sheet = wb2['Teaching Assistant Records']
    tas = {}
    j=0
    lastRow = sheet.max_row
    for i in sheet["A2":"F"+str(lastRow)]:
        tas[j] = {"Name": i[1].value+" "+i[0].value, "Period1": i[2].value, "Period2": i[3].value, "Period3": i[4].value, "Period4": i[5].value}
        #print(tas[j])
        j+=1
    return tas

def studentList():
    sheet = wb2['Student Records']
    studentRecord = {}
    lastRow = sheet.max_row
    for i in sheet["A2":"J581"]:
        studentRecord[i[0].value] = {"StudentID": i[0].value, "Name": i[2].value+" "+i[1].value, "Grade": i[3].value, "ClassP1": i[4].value, "ClassP2": i[5].value, "ClassP3": i[6].value, "ClassP4": i[7].value, "healthFlag": i[8].value, "ECs": i[9].value}
        #print(studentRecord[i[0].value]["Name"])
    return studentRecord

print(studentList())
>>>>>>> Stashed changes
