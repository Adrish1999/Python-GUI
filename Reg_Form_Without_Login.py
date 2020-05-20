import datetime
import tkinter.messagebox as tm
from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk,Image

path="logo1.png"

sum=0


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=1328, height=455)


def Numberonly1(event):
    global sum
    item1 = (m1.get())
    sum += item1


def Numberonly2(event):
    global sum
    item2 = (m2.get())
    sum += item2


def Numberonly3(event):
    global sum
    item3 = (m3.get())
    sum += item3


def Numberonly4(event):
    global sum
    item4 = (m4.get())
    sum += item4


def Numberonly5(event):
    global sum
    item5 = (m5.get())
    sum += item5


def Numberonly6(event):
    global sum
    item6 = (m6.get())
    sum += item6


def Numberonly16():
    global sum
    s.set(sum)
    avg = (sum / 6)
    answer.set(round(avg, 2))


def logged():
    s = str(datetime.datetime.now())
    tm.showinfo("Log", "Entry created successfully at " + s)


def Database():
    global conn, cursor
    conn = sqlite3.connect("Student.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUDENT (SNO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FirstName TEXT, MiddleName TEXT, LastName TEXT, DateOfBirth INTEGER, MonthOfBirth TEXT, YearOfBirth INTEGER, Gender TEXT, EmailID TEXT, Contact1 TEXT, Contact2 TEXT, Hobbies TEXT, PermanentAddress TEXT, Pincode TEXT, Locality TEXT, City TEXT, PO TEXT, PS TEXT, Lifestyle TEXT, State TEXT, Country TEXT, ParentsName TEXT, ParentsAddress TEXT, ParentsOccupation TEXT, ParentsContact TEXT, ParentsEmail TEXT, GuardianName TEXT, GuardianAddress TEXT, GuardianOccupation TEXT, GuardianContact TEXT, GuardianEmail TEXT, Class12Stream TEXT, English INTEGER, Vernacular INTEGER, Mathematics INTEGER, Physics INTEGER, Chemistry INTEGER, ComputerScience INTEGER, Class12Percentage INTEGER, Class12Aggregate INTEGER)")
    conn.commit()

def Errorcheck1(event):
    str1 = firstname.get()
    for i in range(len(str1)):
        p1 = str1[i]
        p2 = ord(p1)
        if ((p2 < 65) or ((p2 > 90) and (p2 < 97)) or (p2 > 122)):
            tm.showerror("Error", "Invalid First Name")
            tm.showinfo("my message", "Re-enter your first name")
            firstname.set("")
            break

def Errorcheck2(event):
    str1 = middlename.get()
    for i in range(len(str1)):
        p1 = str1[i]
        p2 = ord(p1)
        if ((p2 < 65) or ((p2 > 90) and (p2 < 97)) or (p2 > 122)):
            tm.showerror("Error", "Invalid Middle Name")
            tm.showinfo("my message", "Re-enter your Middle name")
            middlename.set("")
            break

def Errorcheck3(event):
    str1 = lastname.get()
    for i in range(len(str1)):
        p1 = str1[i]
        p2 = ord(p1)
        if ((p2 < 65) or ((p2 > 90) and (p2 < 97)) or (p2 > 122)):
            tm.showerror("Error", "Invalid Last Name")
            tm.showinfo("my message", "Re-enter your Middle name")
            lastname.set("")
            break

def Errorcheck9(event):
    str1 = parent.get()
    for i in range(len(str1)):
        p1 = str1[i]
        p2 = ord(p1)
        if ((p2 < 65) or ((p2 > 90) and (p2 < 97)) or (p2 > 122) or (p2!=32)):
            tm.showerror("Error", "Invalid Parents Name")
            tm.showinfo("my message", "Re-enter your Parents name")
            parent.set("")
            break

def Errorcheck10(event):
    str1 = guardian.get()
    for i in range(len(str1)):
        p1 = str1[i]
        p2 = ord(p1)
        if ((p2 < 65) or ((p2 > 90) and (p2 < 97)) or (p2 > 122) or (p2!=32)):
            tm.showerror("Error", "Invalid Guardian Name")
            tm.showinfo("my message", "Re-enter your Guardian name")
            guardian.set("")
            break

def Errorcheck4(event):
    try:
        str1 = int(cl6a.get())
        str2 = cl6b.get()
        str3 = int(cl6c.get())
        if(type(str1) is not int or type(str3) is not int):
            raise ValueError("Error in type occured")
        if ((str3 % 400 == 0) or (str3 % 4 == 0 and str3 % 100 != 0)):
            pc = 1
        else:
            pc = 0
        if (((str1 > 28) and (str2 == "February") and (pc == 0))):
            tm.showerror("Error", "Invalid Date Entered")
            tm.showinfo("my message", "Re-enter your Date Of Birth")
            cl6a.set("")
            cl6b.set("")
            cl6c.set("")
    except ValueError as ve:
        print(ve)





def Errorcheck5(event):
    str1 = phone1.get()
    if(len(str1)>10):
        tm.showerror("Error", "Invalid Contact Number Entered")
        tm.showinfo("my message", "Re-enter your Contact Number")
        phone1.set("")


def Errorcheck7(event):
    str1 = phone3.get()
    if (len(str1) > 10):
        tm.showerror("Error", "Invalid Contact Number Entered")
        tm.showinfo("my message", "Re-enter your Contact Number")
        phone3.set("")


def Errorcheck6(event):
    str1 = phone2.get()
    if (len(str1) > 10):
        tm.showerror("Error", "Invalid Contact Number Entered")
        tm.showinfo("my message", "Re-enter your Contact Number")
        phone2.set("")

def Errorcheck8(event):
    str1 = phone4.get()
    if (len(str1) > 10):
        tm.showerror("Error", "Invalid Contact Number Entered")
        tm.showinfo("my message", "Re-enter your Contact Number")
        phone4.set("")


def DatabaseAdd():
    Database()
    global conn, cursor
    cursor.execute(
        "INSERT INTO STUDENT(FirstName, MiddleName, LastName, DateOfBirth, MonthOfBirth, YearOfBirth, Gender, EmailID, Contact1, Contact2, Hobbies, PermanentAddress, Pincode, Locality, City, PO, PS, Lifestyle, State, Country, ParentsName, ParentsAddress, ParentsOccupation, ParentsContact, ParentsEmail, GuardianName, GuardianAddress, GuardianOccupation, GuardianContact, GuardianEmail, Class12Stream, English, Vernacular, Mathematics, Physics, Chemistry, ComputerScience, Class12Percentage, Class12Aggregate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (str(firstname.get()), str(middlename.get()), str(lastname.get()), str(cl6a.get()), str(cl6b.get()),
         str(cl6c.get()), str(i1.get()), str(email1.get()), str(phone1.get()), str(phone2.get()), str(hobby.get()),
         str(address1.get()), str(pincode.get()), str(locality.get()), str(city.get()), str(po.get()),
         str(ps.get()), str(i2.get()), str(state.get()), str(cl7a.get()), str(parent.get()),
         str(parentaddress.get()), str(parentoccupation.get()), str(phone3.get()), str(email2.get()),
         str(guardian.get()), str(guardaddress.get()), str(guardoccupation.get()), str(phone4.get()),
         str(email3.get()), str(c31a.get()), str(m1.get()), str(m2.get()), str(m3.get()), str(m4.get()),
         str(m5.get()), str(m6.get()), str(answer.get()), str(s.get())))
    conn.commit()
    firstname.set(""), middlename.set(""), lastname.set(""), cl6a.set(""), cl6b.set(""), cl6c.set(""), i1.set(
        ""), email1.set(""), phone1.set(""), phone2.set(""), hobby.set(""), address1.set(""), pincode.set(
        ""), locality.set(""), city.set(""), po.set(""), ps.set(""), i2.set(""), state.set(""), cl7a.set(
        ""), parent.set(""), parentaddress.set(""), parentoccupation.set(""), phone3.set(""), email2.set(
        ""), guardian.set(""), guardaddress.set(""), guardoccupation.set(""), phone4.set(""), email3.set(
        ""), c31a.set(""), m1.set("0"), m2.set("0"), m3.set("0"), m4.set("0"), m5.set("0"), m6.set("0"), answer.set(
        "0"), s.set("0")
    cursor.close()
    conn.close()
    logged()


def DatabaseView():
    Database()
    frame1 = Toplevel()
    global conn, cursor
    frame1.title("View Contents")
    w = 450
    h = 75
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    frame1.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def Viewall():
        Database()
        ViewFrame = Toplevel()
        cursor.execute("SELECT * FROM STUDENT")
        conn.commit()
        fetch = cursor.fetchall()
        scrollbarx = Scrollbar(ViewFrame, orient=HORIZONTAL)
        scrollbary = Scrollbar(ViewFrame, orient=VERTICAL)
        tree = ttk.Treeview(ViewFrame, columns=(
            "SNo", "FirstName", "MiddleName", "LastName", "DateOfBirth", "MonthOfBirth", "YearOfBirth", "Gender",
            "EmailID", "Contact1", "Contact2", "Hobbies", "PermanentAddress", "Pincode", "Locality", "City", "PO", "PS",
            "Lifestyle", "State", "Country", "ParentsName", "ParentsAddress", "ParentsOccupation", "ParentsContact",
            "ParentsEmail", "GuardianName", "GuardianAddress", "GuardianOccupation", "GuardianContact", "GuardianEmail",
            "Class12Stream", "English", "Vernacular", "Mathematics", "Physics", "Chemistry", "ComputerScience",
            "Class12Percentage", "Class12Aggregate"),
                            selectmode=EXTENDED, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('SNo', text="SNo", anchor=CENTER), tree.heading('FirstName', text="FirstName",
                                                                     anchor=CENTER), tree.heading('MiddleName',
                                                                                                  text="MiddleName",
                                                                                                  anchor=CENTER), tree.heading(
            'LastName', text="LastName", anchor=CENTER), tree.heading('DateOfBirth', text="DateOfBirth",
                                                                      anchor=CENTER), tree.heading('MonthOfBirth',
                                                                                                   text="MonthOfBirth",
                                                                                                   anchor=CENTER), tree.heading(
            'YearOfBirth', text="YearOfBirth", anchor=CENTER), tree.heading('Gender', text="Gender",
                                                                            anchor=CENTER), tree.heading('EmailID',
                                                                                                         text="EmailID",
                                                                                                         anchor=CENTER), tree.heading(
            'Contact1', text="Contact1", anchor=CENTER), tree.heading('Contact2', text="Contact2",
                                                                      anchor=CENTER), tree.heading('Hobbies',
                                                                                                   text="Hobbies",
                                                                                                   anchor=CENTER), tree.heading(
            'PermanentAddress', text="PermanentAddress", anchor=CENTER), tree.heading('Pincode', text="Pincode",
                                                                                      anchor=CENTER), tree.heading(
            'Locality', text="Locality", anchor=CENTER), tree.heading('City', text="City",
                                                                      anchor=CENTER), tree.heading('PO', text="PO",
                                                                                                   anchor=CENTER), tree.heading(
            'PS', text="PS", anchor=CENTER), tree.heading('Lifestyle', text="Lifestyle",
                                                          anchor=CENTER), tree.heading('State', text="State",
                                                                                       anchor=CENTER), tree.heading(
            'Country', text="Country", anchor=CENTER), tree.heading('ParentsName', text="ParentsName",
                                                                    anchor=CENTER), tree.heading('ParentsAddress',
                                                                                                 text="ParentsAddress",
                                                                                                 anchor=CENTER), tree.heading(
            'ParentsOccupation', text="ParentsOccupation", anchor=CENTER), tree.heading('ParentsContact',
                                                                                        text="ParentsContact",
                                                                                        anchor=CENTER), tree.heading(
            'ParentsEmail', text="ParentsEmail", anchor=CENTER), tree.heading('GuardianName', text="GuardianName",
                                                                              anchor=CENTER), tree.heading(
            'GuardianAddress', text="GuardianAddress", anchor=CENTER), tree.heading('GuardianOccupation',
                                                                                    text="GuardianOccupation",
                                                                                    anchor=CENTER), tree.heading(
            'GuardianContact', text="GuardianContact", anchor=CENTER), tree.heading('GuardianEmail',
                                                                                    text="GuardianEmail",
                                                                                    anchor=CENTER), tree.heading(
            'Class12Stream', text="Class12Stream", anchor=CENTER), tree.heading('English', text="English",
                                                                                anchor=CENTER), tree.heading(
            'Vernacular', text="Vernacular", anchor=CENTER), tree.heading('Mathematics', text="Mathematics",
                                                                          anchor=CENTER), tree.heading('Physics',
                                                                                                       text="Physics",
                                                                                                       anchor=CENTER), tree.heading(
            'Chemistry', text="Chemistry", anchor=CENTER), tree.heading('ComputerScience', text="ComputerScience",
                                                                        anchor=CENTER), tree.heading(
            'Class12Percentage', text="Class12Percentage", anchor=CENTER), tree.heading('Class12Aggregate',
                                                                                        text="Class12Aggregate",
                                                                                        anchor=CENTER)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0,
                                                                        width=140), tree.column('#2', stretch=NO,
                                                                                                minwidth=0,
                                                                                                width=140), tree.column(
            '#3', stretch=NO, minwidth=0, width=140), tree.column('#4', stretch=NO, minwidth=0,
                                                                  width=140), tree.column('#5', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=140), tree.column(
            '#6', stretch=NO, minwidth=0, width=140), tree.column('#7', stretch=NO, minwidth=0,
                                                                  width=150), tree.column('#8', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=150), tree.column(
            '#9', stretch=NO, minwidth=0, width=150), tree.column('#10', stretch=NO, minwidth=0,
                                                                  width=140), tree.column('#11', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=140), tree.column(
            '#12', stretch=NO, minwidth=0, width=140), tree.column('#13', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#14', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#15', stretch=NO, minwidth=0, width=140), tree.column('#16', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#17', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#18', stretch=NO, minwidth=0, width=140), tree.column('#19', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#20', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#21', stretch=NO, minwidth=0, width=140), tree.column('#22', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#23', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#24', stretch=NO, minwidth=0, width=140), tree.column('#25', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#26', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#27', stretch=NO, minwidth=0, width=140), tree.column('#28', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#29', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#30', stretch=NO, minwidth=0, width=140), tree.column('#31', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#32', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#33', stretch=NO, minwidth=0, width=140), tree.column('#34', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#35', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#36', stretch=NO, minwidth=0, width=140), tree.column('#37', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#38', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#39', stretch=NO, minwidth=0, width=140)
        tree.pack()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def Search():
        Database()
        ViewFrame = Toplevel()
        scrollbarx = Scrollbar(ViewFrame, orient=HORIZONTAL)
        scrollbary = Scrollbar(ViewFrame, orient=VERTICAL)
        tree = ttk.Treeview(ViewFrame, columns=(
            "SNo", "FirstName", "MiddleName", "LastName", "DateOfBirth", "MonthOfBirth", "YearOfBirth", "Gender",
            "EmailID", "Contact1", "Contact2", "Hobbies", "PermanentAddress", "Pincode", "Locality", "City", "P.O",
            "P.S", "Lifestyle", "State", "Country", "ParentsName", "ParentsAddress", "ParentsOccupation",
            "ParentsContact", "ParentsEmail", "GuardianName", "GuardianAddress", "GuardianOccupation",
            "GuardianContact", "GuardianEmail", "Class12Stream", "English", "Vernacular", "Mathematics", "Physics",
            "Chemistry", "ComputerScience", "Class12Percentage", "Class12Aggregate"),
                            selectmode=EXTENDED, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('SNo', text="SNo", anchor=CENTER), tree.heading('FirstName', text="FirstName",
                                                                     anchor=CENTER), tree.heading('MiddleName',
                                                                                                  text="MiddleName",
                                                                                                  anchor=CENTER), tree.heading(
            'LastName', text="LastName", anchor=CENTER), tree.heading('DateOfBirth', text="DateOfBirth",
                                                                      anchor=CENTER), tree.heading('MonthOfBirth',
                                                                                                   text="MonthOfBirth",
                                                                                                   anchor=CENTER), tree.heading(
            'YearOfBirth', text="YearOfBirth", anchor=CENTER), tree.heading('Gender', text="Gender",
                                                                            anchor=CENTER), tree.heading('EmailID',
                                                                                                         text="EmailID",
                                                                                                         anchor=CENTER), tree.heading(
            'Contact1', text="Contact1", anchor=CENTER), tree.heading('Contact2', text="Contact2",
                                                                      anchor=CENTER), tree.heading('Hobbies',
                                                                                                   text="Hobbies",
                                                                                                   anchor=CENTER), tree.heading(
            'PermanentAddress', text="PermanentAddress", anchor=CENTER), tree.heading('Pincode', text="Pincode",
                                                                                      anchor=CENTER), tree.heading(
            'Locality', text="Locality", anchor=CENTER), tree.heading('City', text="City",
                                                                      anchor=CENTER), tree.heading('P.O',
                                                                                                   text="P.O",
                                                                                                   anchor=CENTER), tree.heading(
            'P.S', text="P.S", anchor=CENTER), tree.heading('Lifestyle', text="Lifestyle",
                                                            anchor=CENTER), tree.heading('State', text="State",
                                                                                         anchor=CENTER), tree.heading(
            'Country', text="Country", anchor=CENTER), tree.heading('ParentsName', text="ParentsName",
                                                                    anchor=CENTER), tree.heading('ParentsAddress',
                                                                                                 text="ParentsAddress",
                                                                                                 anchor=CENTER), tree.heading(
            'ParentsOccupation', text="ParentsOccupation", anchor=CENTER), tree.heading('ParentsContact',
                                                                                        text="ParentsContact",
                                                                                        anchor=CENTER), tree.heading(
            'ParentsEmail', text="ParentsEmail", anchor=CENTER), tree.heading('GuardianName', text="GuardianName",
                                                                              anchor=CENTER), tree.heading(
            'GuardianAddress', text="GuardianAddress", anchor=CENTER), tree.heading('GuardianOccupation',
                                                                                    text="GuardianOccupation",
                                                                                    anchor=CENTER), tree.heading(
            'GuardianContact', text="GuardianContact", anchor=CENTER), tree.heading('GuardianEmail',
                                                                                    text="GuardianEmail",
                                                                                    anchor=CENTER), tree.heading(
            'Class12Stream', text="Class12Stream", anchor=CENTER), tree.heading('English', text="English",
                                                                                anchor=CENTER), tree.heading(
            'Vernacular', text="Vernacular", anchor=CENTER), tree.heading('Mathematics', text="Mathematics",
                                                                          anchor=CENTER), tree.heading('Physics',
                                                                                                       text="Physics",
                                                                                                       anchor=CENTER), tree.heading(
            'Chemistry', text="Chemistry", anchor=CENTER), tree.heading('ComputerScience', text="ComputerScience",
                                                                        anchor=CENTER), tree.heading(
            'Class12Percentage', text="Class12Percentage", anchor=CENTER), tree.heading('Class12Aggregate',
                                                                                        text="Class12Aggregate",
                                                                                        anchor=CENTER)
        tree.column('#0', stretch=NO, minwidth=0, width=0), tree.column('#1', stretch=NO, minwidth=0,
                                                                        width=140), tree.column('#2', stretch=NO,
                                                                                                minwidth=0,
                                                                                                width=140), tree.column(
            '#3', stretch=NO, minwidth=0, width=140), tree.column('#4', stretch=NO, minwidth=0,
                                                                  width=140), tree.column('#5', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=140), tree.column(
            '#6', stretch=NO, minwidth=0, width=140), tree.column('#7', stretch=NO, minwidth=0,
                                                                  width=140), tree.column('#8', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=140), tree.column(
            '#9', stretch=NO, minwidth=0, width=140), tree.column('#10', stretch=NO, minwidth=0,
                                                                  width=140), tree.column('#11', stretch=NO,
                                                                                          minwidth=0,
                                                                                          width=140), tree.column(
            '#12', stretch=NO, minwidth=0, width=140), tree.column('#13', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#14', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#15', stretch=NO, minwidth=0, width=140), tree.column('#16', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#17', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#18', stretch=NO, minwidth=0, width=140), tree.column('#19', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#20', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#21', stretch=NO, minwidth=0, width=140), tree.column('#22', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#23', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#24', stretch=NO, minwidth=0, width=140), tree.column('#25', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#26', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#27', stretch=NO, minwidth=0, width=140), tree.column('#28', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#29', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#30', stretch=NO, minwidth=0, width=140), tree.column('#31', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#32', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#33', stretch=NO, minwidth=0, width=140), tree.column('#34', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#35', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#36', stretch=NO, minwidth=0, width=140), tree.column('#37', stretch=NO, minwidth=0,
                                                                   width=140), tree.column('#38', stretch=NO,
                                                                                           minwidth=0,
                                                                                           width=140), tree.column(
            '#39', stretch=NO, minwidth=0, width=140)
        tree.pack()
        if st.get() != "":
            cursor.execute("SELECT * FROM `STUDENT` WHERE `FirstName` LIKE ?", ('%' + str(st.get()) + '%',))
            conn.commit()
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def Reset():
        st.set("")

    Button(frame1, text="View All", command=Viewall).pack(side=LEFT, anchor=N, padx=10, pady=10)
    Button(frame1, text="Search", command=Search).pack(side=LEFT, anchor=N, padx=10, pady=10)
    st = StringVar()
    Entry(frame1, textvariable=st, width=30).pack(side=LEFT, anchor=N, padx=5, pady=11)
    st.get()
    Button(frame1, text="Reset", command=Reset).pack(side=LEFT, anchor=N, padx=10, pady=10)
    frame1.resizable(0, 0)


def Exit():
    result = tm.askquestion('Inventory Management v1.3', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        cursor.close()
        conn.close()
        exit()


def Chnglog():
    tm.showinfo("Changelog",
                "v1.0 - Only GUI \nv1.1 - Accepts inputs and saves it to text file \nv1.2 - Open previous logs\nv1.3 - SQLite3 Database integration")


def About():
    tm.showinfo("About", "Python GUI Project\nInventory Management v1.3")


root = Tk()
sizex = 5000
sizey = 4000
posx = 100
posy = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

# create a drop down menu
menu = Menu(root)
root.title("Student Admission System")
root.config(menu=menu)

# file menu
file = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file)
file.add_command(label="Open File", command=DatabaseView)
file.add_separator()
file.add_command(label="Exit", command=Exit)

# help menu
hlp = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=hlp)
hlp.add_command(label="About", command=About)
hlp.add_command(label="Changelog", command=Chnglog)

myframe = Frame(root, relief=GROOVE, width=sizex, height=sizey, bd=1)
myframe.place(x=5, y=200)

img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(root, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.place(x=40,y=30)


canvas = Canvas(myframe)
frame = Frame(canvas, bg="light blue")
myscrollbar1 = Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar1.set)

myscrollbar1.pack(side="right", fill="y")
myscrollbar2 = Scrollbar(myframe, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=myscrollbar2.set)

myscrollbar2.pack(side="bottom", fill="x")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)

# data()
root.configure(bg="black")
label = Label(root, text="APPLICATION  FORM  OF  ST.THOMAS'  COLLEGE  ")
label.config(font=("Baskerville Old Face", 34, 'bold'), fg="blue")
label.place(x=220, y=75)

l4s = Label(frame, text="Personal Details  :-", bg="green", fg="yellow")
l4s.config(font=("Courier", 25, 'bold'))
l4s.grid(row=3, column=0, pady=50, sticky="W")

l5 = Label(frame, text="First Name", bg="light blue")
l5.config(font=("Aeril", 20))
l5.grid(row=5, column=0)
firstname = StringVar()
el5a = Entry(frame, width=30, textvariable=firstname)
el5a.config(font=("Aeril", 15))
el5a.bind('<Leave>',Errorcheck1)
el5a.grid(row=5, column=1, sticky="W", columnspan=2)

l5b = Label(frame, text="Middle Name", bg="light blue")
l5b.config(font=("Aeril", 20))
l5b.grid(row=6, column=0, pady=50)
middlename = StringVar()
el5b = Entry(frame, width=30, textvariable=middlename)
el5b.config(font=("Aeril", 15))
el5b.bind('<Leave>',Errorcheck2)
el5b.grid(row=6, column=1, sticky="W", columnspan=2)

l5c = Label(frame, text="Last Name", bg="light blue")
l5c.config(font=("Aeril", 20))
l5c.grid(row=7, column=0)
lastname = StringVar()
el5c = Entry(frame, width=30, textvariable=lastname)
el5c.config(font=("Aeril", 15))
el5c.bind('<Leave>',Errorcheck3)
el5c.grid(row=7, column=1, sticky="W", columnspan=2)

# DATE OF BIRTH
l6 = Label(frame, text="Date Of Birth", bg="light blue")
l6.config(font=("Aerial", 20))
l6.grid(row=8, column=0, pady=50)
cl6a = ttk.Combobox(frame, values=[i for i in range(1, 32)])
cl6a.set("DATE")
cl6a.bind("<<ComboboxSelected>>")
cl6a.config(font=("Aerial", 15), width='15')
cl6a.grid(row=8, column=1, sticky="W", columnspan=2)
cl6b = ttk.Combobox(frame,
                    values=["January", "February", "March", "April", "May", "June", "July", "August", "September",
                            "October", "November", "December"])
cl6b.set("MONTH")
cl6b.bind("<<ComboboxSelected>>")
cl6b.config(font=("Aerial", 15), width='15')
cl6b.place(x=690, y=411)
cl6c = ttk.Combobox(frame, values=[i for i in range(1975, 2019)])
cl6c.bind('<Leave>',Errorcheck4)
cl6c.set("YEAR")
cl6c.bind("<<ComboboxSelected>>")
cl6c.config(font=("Aerial", 15), width='15')
cl6c.place(x=920, y=411)

# GENDER
l7 = Label(frame, text="Gender", bg="light blue")
l7.config(font=("Aerial", 20))
l7.grid(row=9, column=0)
i1 = StringVar()
r1 = Radiobutton(frame, text="Male", value="Male", variable=i1)
r1.config(font=("Aerial", 15))
r1.grid(row=9, column=1, sticky="W", columnspan=2)
r2 = Radiobutton(frame, text="Female", value="Female", variable=i1)
r2.config(font=("Aerial", 15))
r2.place(x=610, y=496)
r3 = Radiobutton(frame, text="Others", value="Others", variable=i1)
r3.config(font=("Aerial", 15))
r3.place(x=780, y=496)

# EMAIL
l8 = Label(frame, text="Email ID", bg="light blue")
l8.config(font=("Aerial", 20))
l8.grid(row=10, column=0, pady=40)
email1 = StringVar()
el8 = Entry(frame, width=50, textvariable=email1)
el8.config(font=("Aeril", 15))
el8.grid(row=10, column=1, sticky="W")
# CONTACT NO 1
l9 = Label(frame, text="Contact Number 1", bg="light blue")
l9.config(font=("Aerial", 20))
l9.grid(row=11, column=0)
phone1 = StringVar()
el9 = Entry(frame, width=30, textvariable=phone1)
el9.bind('<Leave>',Errorcheck5)
el9.config(font=("Aeril", 15))
el9.grid(row=11, column=1, sticky="W")

# CONTACT NO 2
l10 = Label(frame, text="Contact Number 2", bg="light blue")
l10.config(font=("Aerial", 20))
l10.grid(row=12, column=0, pady=40)
phone2 = StringVar()
el10 = Entry(frame, width=30, textvariable=phone2)
el10.config(font=("Aeril", 15))
el10.bind('<Leave>',Errorcheck6)
el10.grid(row=12, column=1, sticky="W")

# HOBBIES
l11 = Label(frame, text="Hobbies", bg="light blue")
l11.config(font=("Aerial", 20))
l11.grid(row=14, column=0)
hobby = StringVar()
el11 = Entry(frame, width=50, textvariable=hobby)
el11.config(font=("Aeril", 15))
el11.grid(row=14, column=1, sticky="W")

l4s = Label(frame, text="Residential Details  :-", bg="green", fg="yellow")
l4s.config(font=("Courier", 25, 'bold'))
l4s.grid(row=15, column=0, pady=50)

# PERMANENT ADDRESS
l12 = Label(frame, text="Permanent Address", bg="light blue")
l12.config(font=("Aerial", 20))
l12.grid(row=17, column=0)
address1 = StringVar()
el12 = Entry(frame, width=80, textvariable=address1)
el12.config(font=("Aeril", 15))
el12.grid(row=17, column=1, sticky="W")

# PINCODE
l13 = Label(frame, text="Pincode", bg="light blue")
l13.config(font=("Aerial", 20))
l13.grid(row=18, column=0, pady=50)
pincode = StringVar()
el13 = Entry(frame, width=15, textvariable=pincode)
el13.config(font=("Aeril", 15))
el13.grid(row=18, column=1, sticky="W")

# LOCALITY
l14 = Label(frame, text="Locality", bg="light blue")
l14.config(font=("Aerial", 20))
l14.grid(row=20, column=0)
locality = StringVar()
el14 = Entry(frame, width=20, textvariable=locality)
el14.config(font=("Aeril", 15))
el14.grid(row=20, column=1, sticky="W")
# CITY
l12 = Label(frame, text="City", bg="light blue")
l12.config(font=("Aerial", 20))
l12.grid(row=22, column=0, pady=45)
city = StringVar()
el12 = Entry(frame, width=20, textvariable=city)
el12.config(font=("Aeril", 15))
el12.grid(row=22, column=1, sticky="W")

# PO
l13 = Label(frame, text="Post Office(P.O)", bg="light blue")
l13.config(font=("Aerial", 20))
l13.grid(row=24, column=0)
po = StringVar()
el13 = Entry(frame, width=20, textvariable=po)
el13.config(font=("Aeril", 15))
el13.place(x=462, y=1335)

# PS
l14 = Label(frame, text="Police Station(P.S)", bg="light blue")
l14.config(font=("Aerial", 20))
l14.place(x=850, y=1330)
ps = StringVar()
el14 = Entry(frame, width=20, textvariable=ps)
el14.config(font=("Aeril", 15))
el14.place(x=1182, y=1335)

# Urban/rural
l15 = Label(frame, text="Lifestyle", bg="light blue")
l15.config(font=("Aerial", 20))
l15.grid(row=30, column=0, pady=45)

i2 = StringVar()
r1 = Radiobutton(frame, text="Urban", value="Urban", variable=i2)
r1.config(font=("Aerial", 15))
r1.grid(row=30, column=1, sticky="W", columnspan=2)
r2 = Radiobutton(frame, text="Rural", value="Rural", variable=i2)
r2.config(font=("Aerial", 15))
r2.place(x=600, y=1413)

# State
l16 = Label(frame, text="State", bg="light blue")
l16.config(font=("Aerial", 20,))
l16.grid(row=31, column=0, pady=10)
state = StringVar()
el16 = Entry(frame, width=20, textvariable=state)
el16.config(font=("Aeril", 15))
el16.grid(row=31, column=1, sticky="W")

# Country
l17 = Label(frame, text="Country", bg="light blue")
l17.config(font=("Aerial", 20,))
l17.grid(row=32, column=0, pady=30)
cl7a = ttk.Combobox(frame, values=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Barbuda",
                                   "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
                                   "Bahrai", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
                                   "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
                                   "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
                                   "Canada", "Central African Republic (CAR)", "Chad", "Chile", "China", "Colombia",
                                   "Comoros", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia",
                                   "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
                                   "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
                                   "Eswatini (formerly Swaziland)", "Ethiopia", "Fiji", "Finland", "France",
                                   "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
                                   "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
                                   "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
                                   "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo",
                                   "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
                                   "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
                                   "Malaysia", "Maldives", "Mali", "Malt", "Marshall Islands", "Mauritius",
                                   "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
                                   "Mozambique", "Myanmar(formerly Burma)", "Namibia", "Nauru"
    , "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
                                   "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau",
                                   "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
                                   "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
                                   "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
                                   "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
                                   "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                                   "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan",
                                   "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria",
                                   "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo,Tonga",
                                   "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
                                   "Ukraine", "United Arab Emirates (UAE)", "United Kingdom (UK)",
                                   "United States of America (USA)", "Uruguay", "Uzbekistan", "Vanuatu",
                                   "Vatican City (Holy See)", "Venezuela", "Vietnam", "Yemen", "Zambia",
                                   "Zimbabwe"])
cl7a.set("Select A Country")
cl7a.bind("<<ComboboxSelected>>")
cl7a.config(font=("Aerial", 15), width='30')
cl7a.grid(row=32, column=1, sticky="W", columnspan=2)

l18s = Label(frame, text="Parents' Details  :-")
l18s.config(font=("Courier", 25, 'bold'))
l18s.grid(row=33, column=0, pady=40, sticky="W")

# Parent's name
l19 = Label(frame, text="Parents Name", bg="light blue")
l19.config(font=("Aerial", 20,))
l19.grid(row=34, column=0, pady=10)
parent = StringVar()
el19 = Entry(frame, width=20, textvariable=parent)
el19.config(font=("Aeril", 15))
el19.grid(row=34, column=1, sticky="W")

# Parent's address
l20 = Label(frame, text="Parents Address", bg="light blue")
l20.config(font=("Aerial", 20,))
l20.grid(row=35, column=0, pady=30)
parentaddress = StringVar()
el20 = Entry(frame, width=30, textvariable=parentaddress)
el20.config(font=("Aeril", 15))
el20.grid(row=35, column=1, sticky="W")

# Parent's occupation
l21 = Label(frame, text="Parents Occupation", bg="light blue")
l21.config(font=("Aerial", 20,))
l21.grid(row=36, column=0, pady=20)
parentoccupation = StringVar()
el21 = Entry(frame, width=20, textvariable=parentoccupation)
el21.config(font=("Aeril", 15))
el21.grid(row=36, column=1, sticky="W")

# Parents' contact
l22 = Label(frame, text="Parents Contact", bg="light blue")
l22.config(font=("Aerial", 20,))
l22.grid(row=37, column=0, pady=20)
phone3 = StringVar()
el22 = Entry(frame, width=20, textvariable=phone3)
el22.config(font=("Aeril", 15))
el22.bind('<Leave>',Errorcheck7)
el22.grid(row=37, column=1, sticky="W")

# Parents' email
l23 = Label(frame, text="Parents Email", bg="light blue")
l23.config(font=("Aerial", 20,))
l23.grid(row=38, column=0, pady=20)
email2 = StringVar()
el23 = Entry(frame, width=20, textvariable=email2)
el23.config(font=("Aeril", 15))
el23.grid(row=38, column=1, sticky="W")

# Guardian's Name
l24 = Label(frame, text="Guardian Name", bg="light blue")
l24.config(font=("Aerial", 20,))
l24.grid(row=39, column=0, pady=30)
guardian = StringVar()
el24 = Entry(frame, width=20, textvariable=guardian)
el24.config(font=("Aeril", 15))
el24.grid(row=39, column=1, sticky="W")

# Guardian's address
l25 = Label(frame, text="Guardian Address", bg="light blue")
l25.config(font=("Aerial", 20,))
l25.grid(row=40, column=0, pady=20)
guardaddress = StringVar()
el25 = Entry(frame, width=30, textvariable=guardaddress)
el25.config(font=("Aeril", 15))
el25.grid(row=40, column=1, sticky="W")

# Guardians' occupation
l26 = Label(frame, text="Guardian Occupation", bg="light blue")
l26.config(font=("Aerial", 20,))
l26.grid(row=41, column=0, pady=20)
guardoccupation = StringVar()
el26 = Entry(frame, width=20, textvariable=guardoccupation)
el26.config(font=("Aeril", 15))
el26.grid(row=41, column=1, sticky="W")

# Guardians' contact
l27 = Label(frame, text="Guardian Contact", bg="light blue")
l27.config(font=("Aerial", 20,))
l27.grid(row=42, column=0, pady=20)
phone4 = StringVar()
el27 = Entry(frame, width=20, textvariable=phone4)
el27.config(font=("Aeril", 15))
el27.bind('<Leave>',Errorcheck8)
el27.grid(row=42, column=1, sticky="W")

# Guardians' email
l28 = Label(frame, text="Guardian Email", bg="light blue")
l28.config(font=("Aerial", 20,))
l28.grid(row=43, column=0, pady=20)
email3 = StringVar()
el28 = Entry(frame, width=20, textvariable=email3)
el28.config(font=("Aeril", 15))
el28.grid(row=43, column=1, sticky="W")

l29s = Label(frame, text="Educational Details  :-", bg="green", fg="yellow")
l29s.config(font=("Courier", 25, 'bold'))
l29s.grid(row=44, column=0, pady=40, sticky="W")

# Stream
l30 = Label(frame, text="Class 12 Stream", bg="light blue")
l30.config(font=("Aerial", 20,))
l30.grid(row=45, column=0, pady=30)

c31a = ttk.Combobox(frame, values=["PMC-Comp", "PMC-B", "PMC-Comm", "PMC-Arts"])
c31a.set("Class 12 Stream")
c31a.bind("<<ComboboxSelected>>")
c31a.config(font=("Aerial", 15), width='20')
c31a.grid(row=45, column=1, sticky="W", columnspan=2)

l30 = Label(frame, text="According to selection , choose your subjects and enter corresponding marks",
            bg="light blue")
l30.config(font=("Aerial", 20,))
l30.grid(row=46, column=0, pady=30, columnspan=3, sticky="W")

m1 = IntVar()
m2 = IntVar()
m3 = IntVar()
m4 = IntVar()
m5 = IntVar()
m6 = IntVar()
answer = IntVar()
s = IntVar()
cb1 = Checkbutton(frame, text="English")
cb1.config(font=("Aerial", 15))
cb1.grid(row=47, column=0)
cben1 = Entry(frame, width=10, textvariable=m1)
cben1.config(font=("Aeril", 15))
cben1.bind("<Leave>", Numberonly1)
cben1.grid(row=47, column=1, sticky="W")
cb2 = Checkbutton(frame, text="Vernacular")
cb2.config(font=("Aerial", 15))
cb2.grid(row=48, column=0, pady=45)
cben2 = Entry(frame, width=10, textvariable=m2)
cben2.config(font=("Aeril", 15))
cben2.bind("<Leave>", Numberonly2)
cben2.grid(row=48, column=1, sticky="W")
cb3 = Checkbutton(frame, text="Mathematics")
cb3.config(font=("Aerial", 15))
cb3.grid(row=49, column=0, pady=15)
cben3 = Entry(frame, width=10, textvariable=m3)
cben3.config(font=("Aeril", 15))
cben3.bind("<Leave>", Numberonly3)
cben3.grid(row=49, column=1, sticky="W")
cb4 = Checkbutton(frame, text="Physics")
cb4.config(font=("Aerial", 15))
cb4.grid(row=50, column=0, pady=15)
cben4 = Entry(frame, width=10, textvariable=m4)
cben4.config(font=("Aeril", 15))
cben4.bind("<Leave>", Numberonly4)
cben4.grid(row=50, column=1, sticky="W")
cb5 = Checkbutton(frame, text="Chemistry")
cb5.config(font=("Aerial", 15))
cb5.grid(row=51, column=0, pady=15)
cben5 = Entry(frame, width=10, textvariable=m5)
cben5.config(font=("Aeril", 15))
cben5.bind("<Leave>", Numberonly5)
cben5.grid(row=51, column=1, sticky="W")
cb6 = Checkbutton(frame, text="Computer_Science")
cb6.config(font=("Aerial", 15))
cb6.grid(row=52, column=0, pady=15)
cben6 = Entry(frame, width=10, textvariable=m6)
cben6.config(font=("Aeril", 15))
cben6.bind("<Leave>", Numberonly6)
cben6.grid(row=52, column=1, sticky="W")

cal_but = Button(frame, padx=10, bd=7, font=("Helvetica", 10, "bold"), width=15, text="Calculate Percentage",
                 bg="blue", command=Numberonly16).grid(row=62, column=0, pady=10)
l35 = Label(frame, text="Class 12 percentage", bg="light blue")
l35.config(font=("Aerial", 20,))
l35.grid(row=53, column=0, pady=30)
cben16 = Entry(frame, width=10, textvariable=answer, state=DISABLED)
cben16.config(font=("Aeril", 15))
cben16.grid(row=53, column=1, sticky="W")
l36 = Label(frame, text="Class 12 Aggregate", bg="light blue")
l36.config(font=("Aerial", 20,))
l36.grid(row=54, column=0, pady=30)
cben17 = Entry(frame, width=10, textvariable=s, state=DISABLED)
cben17.config(font=("Aeril", 15))
cben17.grid(row=54, column=1, sticky="W")

cb19 = Checkbutton(frame,
                   text="I agree to the terms and conditions and hereby declare to abide by the rules and regulations of the college",
                   bg="light green")
cb19.config(font=("Aerial", 15))
cb19.grid(row=66, column=0, pady=15, columnspan=3)

sub_but = Button(frame, padx=10, bd=7, font=("Helvetica", 10, "bold"), width=15, text="SUBMIT", bg="red",
                 fg="white", command=DatabaseAdd).grid(row=67, column=0, padx=100)
# Thanks
l16p = Label(frame, text="Thank", bg="light blue")
l16p.config(font=("Aerial", 20))
l16p.grid(row=400, column=750)
# You
l15 = Label(frame, text="You", bg="light blue")
l15.config(font=("Aerial", 20))
l15.grid(row=400, column=800)
# So much
l15 = Label(frame, text="So Much Visit Again", bg="light blue")
l15.config(font=("Aerial", 20))
l15.grid(row=400, column=850)
root.mainloop()



