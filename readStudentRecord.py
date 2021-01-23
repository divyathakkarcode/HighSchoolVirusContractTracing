from openpyxl import load_workbook 
wb2 = load_workbook('OEC2021-School_Record_Book.xlsx') 
sheet = wb2['Student Records']
studentRecordDict = {}
j=0
for i in sheet["A2":"J581"]:
    dict[j] = {"StudentID": i[0].value, "Name": i[2].value+" "+i[1].value, "Grade": i[3].value, "ClassP1": i[4].value, "ClassP2": i[5].value, "ClassP3": i[6].value, "ClassP4": i[7].value, "healthFlag": i[8].value, "ECs": i[9].value}
    print(dict[j])
    j+=1