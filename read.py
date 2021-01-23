from openpyxl import load_workbook 
wb2 = load_workbook('OEC2021-School_Record_Book.xlsx') 
sheet = wb2['ZBY1 Status']
dict = {}
j=0
for i in sheet["A2":"D5"]:
    dict[j] = {"StudentID": i[0].value, "Name": i[2].value+" "+i[1].value, "Infected": 1}
    print(dict[j])
    j+=1