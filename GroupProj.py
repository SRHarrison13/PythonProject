import sqlite3
conn = sqlite3.connect('classDatabase.db')
curs = conn.cursor()
try:
    curs.execute('''CREATE TABLE compClasses (department, class, professor, days met, time, prereq)''')
except:
    #placeholder command
    print()
classes = [('CS','130','Chen','MWF','10:30-11:35','none'),\
           ('CS','140','Rodriguez','TTh','3:00-4:50','CS 130'),\
           ('CS','141','Rodriguez','MWF','11:45-12:50','CS 140'),\
           ('CS','240','Diaz','TTh','1:00-2:50','CS 141'),\
           ('CS','241','Yang','MWF','1:30-2:35','CS 240')
           ]
curs.executemany('INSERT INTO compClasses VALUES (?,?,?,?,?,?)',classes)

class ourDatabase:
    def __init__(self):
        print("Welcome to our database. What would you like to do?")
    def main(self):
        inProg = True
        while inProg:
            print("A: Add a class.")
            print("B: Remove a class.")
            print("C: View available classes.")
            print("Q: Quit program.")
            choice = input()
            if choice == 'a' or choice == 'A':
                self.addClass()
            elif choice == 'b' or choice == 'B':
                self.remClass()
            elif choice == 'c' or choice == 'C':
                self.getClasses()
            else:
                inProg = False
    def addClass(self):
        try:
            dep = input("Please enter the department abbreviation. Example: Computer Science = CS.")
            if len(dep) != 2:
                raise ValueError
        except ValueError:
            incorrect = True
            while incorrect:
                print("Incorrect format, department abbreviation cannot be more than two letters.")
                newDep = input("Please try again.")
                if len(newDep) == 2:
                    break
        try:
            classNum = input("Please enter the class number.")
            if len(classNum) != 3:
                raise ValueError
        except ValueError:
            incorrect = True
            while incorrect:
                print("Class number should not be less than 100, nor greater than 999.")
                newClass = input("Please try again.")
                if len(newClass == 3):
                    break
        try:
            prof = input("Please enter the professor's name.")
            digit = False
            for i in range(len(prof)):
                if str.isdigit(prof[i]):
                    digit = True
            if digit == True:
                raise ValueError
        except ValueError:
            incorrect = True
            while incorrect:
                print("Professor name cannot contain numbers.")
                newProf = input("Please try again.")
                newDig = False
                for i in range(len(newProf)):
                    if str.isdigit(newProf[i]):
                        newDig = True
                if newDig == False:
                    break
        try:
            dates = input("Please enter the days when the class meets. For example, a Monday, Wednesday, Friday class is MWF.")
            if len(dates) > 3:
                raise ValueError
        except ValueError:
            incorrect = True
            while incorrect:
                print("Classes can meet up to three times a week.")
                newDate = input("Please try again.")
                if len(newDate) <= 3:
                    break
        try:
            times = input("Please enter the time when the class meets.")
        except:
            print()
        try:
            preq = input("Please enter prerequisites, if any. If none, type 'none'.")
        except:
            print()
        theNewClass = (dep,classNum,prof,dates,times,preq)
        curs.execute('INSERT INTO compClasses VALUES (?,?,?,?,?,?)',theNewClass)
        print("Class added successfully.")
    def remClass(self):
        theClass = input("Please enter the class you would like to remove.")
        classData = theClass.split(' ')
        curs.execute('DELETE FROM compClasses WHERE department = ? AND class = ?',classData[0],classData[1])
        print("Class removed successfully.")
    def getClasses(self):
        try:
            temp = input("Please enter the department you wish to view classes from.")
            if len(temp) != 2:
                raise ValueError
            dep = (temp,)
        except ValueError:
            incorrect = True
            while incorrect:
                print("Department must be in abbreviation form.")
                newDep = input("Please try again.")
                if len(newDep) == 2:
                    dep =(newDep,)
                    break
        for row in curs.execute('SELECT * FROM compClasses WHERE department=?',dep):
            print(row)

newDat = ourDatabase()
newDat.main()
curs.close()
