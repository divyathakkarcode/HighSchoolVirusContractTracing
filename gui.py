import tkinter as tk
import read

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ZBY1 Infection Status")

    window = tk.Text(root, height=50, width=100)
    window.configure(background='gainsboro')
    window.pack()
    
    # configuring different texts
    window.tag_configure('big', font=('Verdana', 17, 'bold'))
    window.tag_configure('normal', font=('Verdana', 14, 'normal'))

    # adding the section title to window 
    window.insert(tk.END, "\n\tStudents Infected:\n", 'big')

# method for getting the names of the students infected at the start of the day
def infectedStudents():
    # getting all the information for the dictionary
    record = read.infectionList()
    student_names = ""
    for infect_num in range(0, len(record)):
        student_names+= "\t" + record[infect_num]["Name"] + "\n"

    return student_names


window.insert(tk.END, infectedStudents(), 'normal')
tk.mainloop()