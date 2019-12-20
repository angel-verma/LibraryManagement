import random
import tkinter.messagebox
from datetime import datetime
from tkinter import *
from tkinter import ttk
import datetime


class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        # self.root.configure(background="powder blue")

        # Variables
        MType = StringVar()
        Ref = StringVar()
        Title = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        PinCode = StringVar()
        MobileNo = StringVar()
        BookID = StringVar()
        BookTitle = StringVar()
        BookType = StringVar()
        Author = StringVar()
        DateBorrowed = StringVar()
        DueDate = StringVar()
        SellingPrice = StringVar()
        Fine = StringVar()
        DateOverDue = StringVar()
        DaysOnloan = StringVar()
        # Prescription = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Libraray Management System", "Confirm if you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        def iReset():
            MType.set(" ")
            Ref.set("")
            Title.set("")
            FirstName.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PinCode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DueDate.set("")
            SellingPrice.set("")
            Fine.set("")
            DateOverDue.set("")
            DaysOnloan.set("")

        def iDelete():
            iReset()
            self.txtDisplayRight.delete("1.0", END)
            self.txtDisplayBottom.delete("1.0", END)

        def iDisplayData():
            self.txtDisplayBottom.insert(END, MType.get()+"\t\t"+Ref.get()+"\t"+Title.get()+"\t" +
                                         FirstName.get()+"\t"+Surname.get()+"\t"+Address1.get()+"\t"+Address2.get()+"\t" +
                                         PinCode.get()+"\t", BookTitle.get()+"\t"+DateBorrowed.get()+"\t"+DaysOnloan.get()+"\n")

        def iReceipt():
            self.txtDisplayRight.insert(
                END, "Member Type :\t\t"+MType.get()+"\n")
            self.txtDisplayRight.insert(END, "Ref No :\t\t"+Ref.get()+"\n")
            self.txtDisplayRight.insert(END, "Title :\t\t"+Title.get()+"\n")
            self.txtDisplayRight.insert(
                END, "First Name :\t\t"+FirstName.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Surname :\t\t"+Surname.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Address1 :\t\t"+Address1.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Address2 :\t\t"+Address2.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Pin Code :\t\t"+PinCode.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Mobile No :\t\t"+MobileNo.get()+"\n")
            self.txtDisplayRight.insert(END, "Book ID :\t\t"+BookID.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Book Title :\t\t"+BookTitle.get()+"\n")
            self.txtDisplayRight.insert(END, "Author :\t\t"+Author.get()+"\n")
            self.txtDisplayRight.insert(
                END, "Date Borrowed :\t\t"+DateBorrowed.get()+"\n")
        # ================================Frame=======================================
        mainFrame = Frame(self.root)
        mainFrame.grid()

        titleFrame = Frame(mainFrame, bd=20, relief=RIDGE)
        titleFrame.pack(side=TOP)

        self.lblTitle = Label(titleFrame, font="arial 40 bold", padx=70,
                              text="\tLibrary Management System\t")
        self.lblTitle.grid()

        dataFrame = Frame(mainFrame, height=400, bd=20, relief=RIDGE)
        dataFrame.pack(side=TOP)

        dataFrameleft = LabelFrame(dataFrame,
                                   height=400, bd=20, pady=20, relief=RIDGE, font="arial 12 bold", text="Library Membership Info:")
        dataFrameleft.pack(side=LEFT)

        dataFrameright = LabelFrame(dataFrame,
                                    height=300, bd=20, relief=RIDGE, font="arial 12 bold", text="Book Details:")
        dataFrameright.pack(side=RIGHT)

        frameDetails = Frame(mainFrame, width=1350,
                             height=100, padx=70, bd=20, relief=RIDGE)
        frameDetails.pack(side=TOP)

        buttonFrame = Frame(mainFrame, width=1350, height=50,
                            bd=20, relief=RIDGE, padx=25)
        buttonFrame.pack(side=BOTTOM)

# =========================================widget===============================================
        self.lblMemberType = Label(
            dataFrameleft, font="arial 12 bold", text="Member Type", padx=2, pady=2)
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.cboMemberType = ttk.Combobox(
            dataFrameleft, font="arial 12 bold", state="readonly", width=23, textvariable=MType)
        self.cboMemberType['value'] = (
            '', 'Student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0, column=1)

        self.lblRefNo = Label(
            dataFrameleft, font="arial 12 bold", text="Reference No", padx=2, pady=2)
        self.lblRefNo.grid(row=1, column=0, sticky=W)
        self.entRefNo = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Ref)
        self.entRefNo.grid(row=1, column=1)

        self.lblTitle = Label(
            dataFrameleft, font="arial 12 bold", text="Title", padx=2, pady=2)
        self.lblTitle.grid(row=2, column=0, sticky=W)
        self.cboTitle = ttk.Combobox(
            dataFrameleft, font="arial 12 bold", state="readonly", width=23, textvariable=Title)
        self.cboTitle['value'] = (
            '', 'Mr.', 'Mrs.', 'Miss', 'Dr')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblName = Label(
            dataFrameleft, font="arial 12 bold", text="FirstName", padx=2, pady=2)
        self.lblName.grid(row=3, column=0, sticky=W)
        self.entFirstName = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=FirstName)
        self.entFirstName.grid(row=3, column=1)

        self.lblSurname = Label(
            dataFrameleft, font="arial 12 bold", text="Surname", padx=2, pady=2)
        self.lblSurname.grid(row=4, column=0, sticky=W)
        self.entSurname = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Surname)
        self.entSurname.grid(row=4, column=1)

        self.lblAddress1 = Label(
            dataFrameleft, font="arial 12 bold", text="Address1:", padx=2, pady=2)
        self.lblAddress1.grid(row=5, column=0, sticky=W)
        self.entAddress1 = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Address1)
        self.entAddress1.grid(row=5, column=1)

        self.lblAddress2 = Label(
            dataFrameleft, font="arial 12 bold", text="Address2:", padx=2, pady=2)
        self.lblAddress2.grid(row=6, column=0, sticky=W)
        self.entAddress2lblAddress2 = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Address2)
        self.entAddress2lblAddress2.grid(row=6, column=1)

        self.lblPinCode = Label(
            dataFrameleft, font="arial 12 bold", text="Pin Code", padx=2, pady=2)
        self.lblPinCode.grid(row=7, column=0, sticky=W)
        self.entPinCode = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=PinCode)
        self.entPinCode.grid(row=7, column=1)

        self.lblMobile = Label(
            dataFrameleft, font="arial 12 bold", text="Mobile No", padx=2, pady=2)
        self.lblMobile.grid(row=8, column=0, sticky=W)
        self.entMobile = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=MobileNo)
        self.entMobile.grid(row=8, column=1)
        # --------------------------------------------------------------------------------------
        self.lblBookId = Label(
            dataFrameleft, font="arial 12 bold", text="Book ID", padx=2, pady=2)
        self.lblBookId.grid(row=0, column=2, sticky=W)
        self.entBookId = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=BookID)
        self.entBookId.grid(row=0, column=3)

        self.lblBookTitle = Label(
            dataFrameleft, font="arial 12 bold", text="Book Title", padx=2, pady=2)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.entBookTitle = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=BookTitle)
        self.entBookTitle.grid(row=1, column=3)

        self.lblAuthor = Label(
            dataFrameleft, font="arial 12 bold", text="Author", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.entAuthor = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Author)
        self.entAuthor.grid(row=2, column=3)

        self.lblDateBorrow = Label(
            dataFrameleft, font="arial 12 bold", text="Date Borrowed", padx=2, pady=2)
        self.lblDateBorrow.grid(row=3, column=2, sticky=W)
        self.entDateBorrow = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=DateBorrowed)
        self.entDateBorrow.grid(row=3, column=3)

        self.lblDateDue = Label(
            dataFrameleft, font="arial 12 bold", text="Date Due", padx=2, pady=2)
        self.lblDateDue.grid(row=4, column=2, sticky=W)
        self.entDateDue = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=DueDate)
        self.entDateDue.grid(row=4, column=3)

        self.lblDaysOnLoan = Label(
            dataFrameleft, font="arial 12 bold", text="Days on Loan", padx=2, pady=2)
        self.lblDaysOnLoan.grid(row=5, column=2, sticky=W)
        self.entDaysOnLoan = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=DaysOnloan)
        self.entDaysOnLoan.grid(row=5, column=3)

        self.lblFine = Label(
            dataFrameleft, font="arial 12 bold", text="Late Return Fine", padx=2, pady=2)
        self.lblFine.grid(row=6, column=2, sticky=W)
        self.entFine = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=Fine)
        self.entFine.grid(row=6, column=3)

        self.lblDateOverDue = Label(
            dataFrameleft, font="arial 12 bold", text="Date Over Due", padx=2, pady=2)
        self.lblDateOverDue.grid(row=7, column=2, sticky=W)
        self.entDateOverDue = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=DateOverDue)
        self.entDateOverDue.grid(row=7, column=3)

        self.lblSellingPrice = Label(
            dataFrameleft, font="arial 12 bold", text="Selling Price", padx=2, pady=2)
        self.lblSellingPrice.grid(row=8, column=2, sticky=W)
        self.entSellingPrice = Entry(
            dataFrameleft, font="arial 12 bold", width=25, textvariable=SellingPrice)
        self.entSellingPrice.grid(row=8, column=3)

        # ===============================Right side widget====================================
        scrollbar = Scrollbar(dataFrameright)
        scrollbar.grid(row=0, column=1, sticky=NS)

        self.txtDisplayRight = Text(
            dataFrameright, font="arial 12 bold", width=32, height=13, padx=8, pady=20)
        self.txtDisplayRight.grid(row=0, column=2)

        listOfBooks = ['Cindrella', 'Game Design', 'Ancient Rome', 'Made in Africa', 'Sleeping Beauty', 'London',
                       'Nigeria', 'Snow White', 'Shreik 3', 'London Street', 'I Love Lagos', 'Love Kenya', 'Hello India']

        def selectBook(event):
            value = str(booklist.get(booklist.curselection()))
            w = value
            if(w == 'Cindrella'):
                BookID.set('ISBN 7869554433')
                BookTitle.set('Cindrella')
                Author.set('Paul Parker')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                # import datetime
                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Game Design'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Game Design')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Ancient Rome'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Ancient Rome')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Made in Africa'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Made in Africa')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Sleeping Beauty'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Sleeping Beauty')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'London'):
                BookID.set('ISBN 67859402')
                BookTitle.set('London')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Nigeria'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Nigeria')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Snow White'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Snow White')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")
# -------------------------------------------------------------
            elif(w == 'Shreik 3'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Shreik 3')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'London Street'):
                BookID.set('ISBN 67859402')
                BookTitle.set('London Street')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'I Love Lagos'):
                BookID.set('ISBN 67859402')
                BookTitle.set('I Love Lagos')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Love Kenya'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Love Kenya')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

            elif(w == 'Hello India'):
                BookID.set('ISBN 67859402')
                BookTitle.set('Hello India')
                Author.set('XYZ')
                Fine.set('Rs.10')
                SellingPrice.set('Rs.50')
                DaysOnloan.set(14)
                iReceipt()

                d1 = datetime.date.today()
                d14 = datetime.timedelta(days=14)
                d2 = (d1+d14)
                DateBorrowed.set(d1)
                DueDate.set(d2)
                DateOverDue.set("NO")

        booklist = Listbox(dataFrameright, width=20,
                           height=12, font="arial 12 bold")
        booklist.bind('<<ListboxSelect>>', selectBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)

        for items in listOfBooks:
            booklist.insert(END, items)

        # ====================================================================================
        self.lblLabel = Label(frameDetails, font="arial 10 bold", pady=8,
                              text="Member Type\tReference No\tTitle\tFirstName\tSurname\tAddress1\tAddress2\tPin Code\tBook Title\tDate Borrowed\tDays on Loan")
        self.lblLabel.grid(row=0, column=0)

        self.txtDisplayBottom = Text(
            frameDetails, font="arial 12 bold", width=130, height=3, padx=2, pady=4)
        self.txtDisplayBottom.grid(row=1, column=0)

        # =====================================buttons========================================
        self.txtDisplayData = Button(
            buttonFrame, text="Display Data", font="arial 12 bold", width=30, bd=4, command=iDisplayData)
        self.txtDisplayData.grid(row=0, column=0)

        self.txtDelete = Button(
            buttonFrame, text="Delete", font="arial 12 bold", width=30, bd=4, command=iDelete)
        self.txtDelete.grid(row=0, column=1)

        self.txtReset = Button(
            buttonFrame, text="Reset", font="arial 12 bold", width=30, bd=4, command=iReset)
        self.txtReset.grid(row=0, column=2)

        self.txtExit = Button(
            buttonFrame, text="Exit", font="arial 12 bold", width=30, bd=4, command=iExit)
        self.txtExit.grid(row=0, column=3)

        # =============================================================================


if __name__ == "__main__":
    root = Tk()
    ob = Library(root)
    root.mainloop()
