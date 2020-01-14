from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time
import sys
# for printing
import tempfile
import win32api
import win32print

def main():
    root = Tk()
    app = Window1(root)

    root.mainloop()

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="Account Login System",
                        font=('arial',50,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        #----------------------------------------------#
        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600,font=('arial',20,'bold')
                                 ,relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600,font=('arial',20,'bold')
                                ,relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0, pady=30)

        #----------------------------------------------#
        self.lblUsername = Label(self.LoginFrame1, text='Username',fg='Cornsilk',
                                 bd=22,font=('arial',20,'bold'), bg='cadet blue')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font=('arial',20,'bold'),
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, padx= 15)

        self.lblPassword = Label(self.LoginFrame1, text='Password',fg='Cornsilk',
                                 bd=22,font=('arial',20,'bold'), bg='cadet blue')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('arial',20,'bold'),
                                 textvariable=self.Password, show='*')
        self.txtPassword.grid(row=1, column=1)

        #----------------------------------------------#

        self.btnLogin = Button(self.LoginFrame2, width=17,font=('arial',20,'bold'),
                               text="Login", command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnReset = Button(self.LoginFrame2, width=17,font=('arial',20,'bold'),
                               command=self.Reset, text="Reset")
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, width=17,font=('arial',20,'bold'),
                               command=self.iExit, text="Exit")
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

        #----------------------------------------------#
    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str(123) and p == str(321)):
            self.master.withdraw()
            self.newWindow = Toplevel(self.master)
            self.newWindow.geometry("1350x750")
            self.app = Customer(self.newWindow)
        else:
            tkinter.messagebox.showinfo("Login Systems", "Invalid login details")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        # self.iExit = tkinter.messagebox.askyesno("Login Systems", "Confirm 'Yes' to exit.")
        # if self.iExit > 0:
        #     self.master.destroy()
        # else:
        #     command = self.new_Window
        #     return
        self.master.destroy()
        return

#----------------------------------------#
class Customer:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, width=1335, height=750,
                           padx=10, bg="powder blue",
                           relief=RIDGE)
        self.frame.pack()


        # ABC = Frame(self.root, bd=10, bg="powder blue", relief=RIDGE)
        ABC = Frame(self.frame, bd=10, bg="powder blue", relief=RIDGE)

        ABC.grid()

        ABC1 = Frame(ABC, bd=14, width=1335, height=100, padx=10, bg="powder blue", relief=RIDGE)
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
        ABC2 = Frame(ABC, bd=14, width=460, height=610, padx=10, bg="cadet blue", relief=RIDGE)
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3 = Frame(ABC, bd=14, width=460, height=610, padx=10, bg="powder blue", relief=RIDGE)
        ABC3.grid(row=1, column=1, sticky=W)
        ABC4 = Frame(ABC, bd=14, width=465, height=610, padx=10, bg="cadet blue", relief=RIDGE)
        ABC4.grid(row=1, column=2, sticky=W)
        ABC5 = Frame(ABC4, bd=14, width=380, height=420, padx=10, bg="cadet blue", relief=RIDGE)
        ABC5.grid(row=0, column=0, sticky=W)
        ABC6 = Frame(ABC4, bd=14, width=380, height=160, padx=10, bg="cadet blue", relief=RIDGE)
        ABC6.grid(row=1, column=0, columnspan=2,sticky=W)

        Date1 = StringVar()
        self.Time1 = StringVar()
        today = datetime.now()

        Date1.set(today.strftime('%Y-%m-%d'))
        self.Time1.set(today.strftime("%H:%M:%S"))

        #----------------------------------------#
        CustomerRef = StringVar()
        FirstName = StringVar()
        SirName = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        CustomerRef.set(random.randint(1980, 9875648))
        CheckInDate.set(today.strftime('%Y-%m-%d'))
        CheckOutDate.set(today.strftime('%Y-%m-%d'))

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()

        E_Latta = StringVar()
        E_Espresso = StringVar()
        E_Iced_Latta = StringVar()
        E_Vale_Coffee = StringVar()
        E_Cappuccino = StringVar()
        E_African_Coffee = StringVar()
        E_American_Coffee = StringVar()
        E_Iced_Cappuccino = StringVar()

        E_Latta.set("0")
        E_Espresso.set("0")
        E_Iced_Latta.set("0")
        E_Vale_Coffee.set("0")
        E_Cappuccino.set("0")
        E_African_Coffee.set("0")
        E_American_Coffee.set("0")
        E_Iced_Cappuccino.set("0")

        #----------------------------------------#
        self.lblDate = Label(ABC1, textvariable=Date1, font=('Arial',30,'bold'), pady=9
                              ,bd=5, bg='Cadet blue', fg="Cornsilk").grid(row=0,column=0)

        self.lblTitle = Label(ABC1, text="\tCustomer Billing System\t\t", font=('Arial', 30, 'bold'), pady=9
                              ,bd=5, bg='Cadet blue', fg="Cornsilk").grid(row=0,column=1)

        self.lblTime = Label(ABC1, textvariable=self.Time1, font=('Arial', 30, 'bold'), pady=9
                              ,bd=5, bg='Cadet blue', fg="Cornsilk")
        self.lblTime.grid(row=0,column=2)

        #----------------------------------------#
        def tick():
            # get the current local time from the PC
            time2 = datetime.now().strftime("%H:%M:%S")

            # if time string has changed, update it
            if time2 != self.Time1:
                self.Time1.set(time2)
                # self.lblTime.config(text=time2)

            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            self.lblTime.after(900, tick)

        tick()

        #----------------------------------------#
        def sendToPrinter(mytext):
            filename = tempfile.mktemp(".txt")
            open (filename, "w").write(mytext)
            win32api.ShellExecute(
              0,
              "print",
              filename,
              #
              # If this is None, the default printer will
              # be used anyway.
              #
              '/d:"%s"' % win32print.GetDefaultPrinter(),
              ".",
              0
            )

            print(filename)

        #----------------------------------------#
        def iExit():
            # iExit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            # if iExit > 0:
            #     root.destroy()
            #     return
            self.master.destroy()
            sys.exit()
            return

        def Reset():
            self.txtReceipt.delete("1.0", END)
            E_Latta.set("0")
            E_Espresso.set("0")
            E_Iced_Latta.set("0")
            E_Vale_Coffee.set("0")
            E_Cappuccino.set("0")
            E_African_Coffee.set("0")
            E_American_Coffee.set("0")
            E_Iced_Cappuccino.set("0")
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            CustomerRef.set("")
            FirstName.set("")
            SirName.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")

        def chkLatta():
            if (var1.get() == 1):
                self.txtLatte.configure(state=NORMAL)
                self.txtLatte.focus()
                self.txtLatte.delete('0', END)
                E_Latta.set("")
            elif var1.get() == 0:
                self.txtLatte.configure(state=DISABLED)
                E_Latta.set("0")

        def chkEspresso():
            if (var2.get() == 1):
                self.txtEspresso.configure(state=NORMAL)
                self.txtEspresso.focus()
                self.txtEspresso.delete('0', END)
                E_Espresso.set("")
            elif var2.get() == 0:
                self.txtEspresso.configure(state=DISABLED)
                E_Espresso.set("0")

        def chkIced_Latta():
            if (var3.get() == 1):
                self.txtIced_Latta.configure(state=NORMAL)
                self.txtIced_Latta.focus()
                self.txtIced_Latta.delete('0', END)
                E_Iced_Latta.set("")
            elif var3.get() == 0:
                self.txtIced_Latta.configure(state=DISABLED)
                E_Iced_Latta.set("0")

        def chkVale_Coffee():
            if (var4.get() == 1):
                self.txtVale_Coffee.configure(state=NORMAL)
                self.txtVale_Coffee.focus()
                self.txtVale_Coffee.delete('0', END)
                E_Vale_Coffee.set("")
            elif var4.get() == 0:
                self.txtVale_Coffee.configure(state=DISABLED)
                E_Vale_Coffee.set("0")

        def chkCappuccino():
            if (var5.get() == 1):
                self.txtCappuccino.configure(state=NORMAL)
                self.txtCappuccino.focus()
                self.txtCappuccino.delete('0', END)
                E_Cappuccino.set("")
            elif var5.get() == 0:
                self.txtCappuccino.configure(state=DISABLED)
                E_Cappuccino.set("0")

        def chkAfrican_Coffee():
            if (var6.get() == 1):
                self.txtAfrican_Coffee.configure(state=NORMAL)
                self.txtAfrican_Coffee.focus()
                self.txtAfrican_Coffee.delete('0', END)
                E_African_Coffee.set("")
            elif var6.get() == 0:
                self.txtAfrican_Coffee.configure(state=DISABLED)
                E_African_Coffee.set("0")

        def chkAmerican_Coffee():
            if (var7.get() == 1):
                self.txtAmerican_Coffee.configure(state=NORMAL)
                self.txtAmerican_Coffee.focus()
                self.txtAmerican_Coffee.delete('0', END)
                E_American_Coffee.set("")
            elif var7.get() == 0:
                self.txtAmerican_Coffee.configure(state=DISABLED)
                E_American_Coffee.set("0")

        def chkIced_Cappuccino():
            if (var8.get() == 1):
                self.txtIced_Cappuccino.configure(state=NORMAL)
                self.txtIced_Cappuccino.focus()
                self.txtIced_Cappuccino.delete('0', END)
                E_Iced_Cappuccino.set("")
            elif var8.get() == 0:
                self.txtIced_Cappuccino.configure(state=DISABLED)
                E_Iced_Cappuccino.set("0")

        def costOfItem():
            CustomerRef.set(random.randint(1980, 9875648))
            self.txtReceipt.delete('1.0', END)

            try:
                Item1 = float(E_Latta.get())
                Item2 = float(E_Espresso.get())
                Item3 = float(E_Iced_Latta.get())
                Item4 = float(E_Vale_Coffee.get())
                Item5 = float(E_Cappuccino.get())
                Item6 = float(E_African_Coffee.get())
                Item7 = float(E_American_Coffee.get())
                Item8 = float(E_Iced_Cappuccino.get())
            except ValueError:
                iMsg = tkinter.messagebox.showwarning("Customer Billing System",
                                                    "Please chek if the values are null or Uncheck the item")
                return


            PriceofDrinks = (Item1 * 1.2) + (Item2 * 2.05) + (Item3 * 1.2)\
                                + (Item4 * 1.99) + (Item5 * 2.99) + (Item6 * 1.89)\
                                + (Item7 * 2.39) + (Item8 * 2.05)

            SubTotalofItems = "$", str('%.2f' % (PriceofDrinks))
            SubTotal.set(SubTotalofItems)
            Tax = "$", str('%.2f' % (PriceofDrinks * 0.15))
            PaidTax.set(Tax)
            TTax = (PriceofDrinks * 0.15)
            TCost = "$", str('%.2f' % (PriceofDrinks + TTax))
            TotalCost.set(TCost)


            self.txtReceipt.insert(END, 'Customer Ref :\t\t' + CustomerRef.get() + "\n")
            self.txtReceipt.insert(END, 'Items\t\t\t\t' + "No of Items \n")
            self.txtReceipt.insert(END, 'Latta\t\t\t\t\t' + E_Latta.get() + "\n")
            self.txtReceipt.insert(END, 'Espresso\t\t\t\t\t' + E_Espresso.get() + "\n")
            self.txtReceipt.insert(END, 'Iced Latta\t\t\t\t\t' + E_Iced_Latta.get() + "\n")
            self.txtReceipt.insert(END, 'Vale Coffee\t\t\t\t\t' + E_Vale_Coffee.get() + "\n")
            self.txtReceipt.insert(END, 'Cappuccino\t\t\t\t\t' + E_Cappuccino.get() + "\n")
            self.txtReceipt.insert(END, 'African Coffee\t\t\t\t\t' + E_African_Coffee.get() + "\n")
            self.txtReceipt.insert(END, 'American Coffee\t\t\t\t\t' + E_American_Coffee.get() + "\n")
            self.txtReceipt.insert(END, 'Iced Cappuccino\t\t\t\t\t' + E_Iced_Cappuccino.get() + "\n")

            self.txtReceipt.insert(END, '\nTax Paid:\t\t\t\t' + PaidTax.get() + "\n")
            self.txtReceipt.insert(END, '\nSubTotal:\t\t\t\t' + str(SubTotal.get()) + "\n")
            self.txtReceipt.insert(END, '\nTotal Cost:\t\t\t\t' +  str(TotalCost.get()))



        #----------------------------------------#
        self.txtReceipt = Text(ABC5, font=('Arial',9,'bold'), width=43, height=29, bd=10)
        self.txtReceipt.grid(row=0,column=0)
        #----------------------------------------#
        self.lblCus_Ref = Label(ABC2, text="Customer Ref", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblCus_Ref.grid(row=0,column=0, sticky= W)
        self.txtCus_Ref = Entry(ABC2, font=('Arial',12,'bold'), textvariable=CustomerRef, width=25)
        self.txtCus_Ref.grid(row=0,column=1, pady=3, padx=20)

        self.lblFirstName = Label(ABC2, text="FirstName", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblFirstName.grid(row=1,column=0, sticky= W)
        self.txtFirstName = Entry(ABC2, font=('Arial',12,'bold'), textvariable=FirstName, width=25)
        self.txtFirstName.grid(row=1,column=1, pady=3, padx=20)

        self.lblSirName = Label(ABC2, text="SirName", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblSirName.grid(row=2,column=0, sticky= W)
        self.txtSirName = Entry(ABC2, font=('Arial',12,'bold'), textvariable=SirName, width=25)
        self.txtSirName.grid(row=2,column=1, pady=3, padx=20)

        self.lblAddress = Label(ABC2, text="Address", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblAddress.grid(row=3,column=0, sticky= W)
        self.txtAddress = Entry(ABC2, font=('Arial',12,'bold'), textvariable=Address, width=25)
        self.txtAddress.grid(row=3,column=1, pady=3, padx=20)

        self.lblPostCode = Label(ABC2, text="PostCode", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblPostCode.grid(row=4,column=0, sticky= W)
        self.txtPostCode = Entry(ABC2, font=('Arial',12,'bold'), textvariable=PostCode, width=25)
        self.txtPostCode.grid(row=4,column=1, pady=3, padx=20)

        self.lblMobile = Label(ABC2, text="Mobile", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblMobile.grid(row=5,column=0, sticky= W)
        self.txtMobile = Entry(ABC2, font=('Arial',12,'bold'), textvariable=Mobile, width=25)
        self.txtMobile.grid(row=5,column=1, pady=3, padx=20)

        self.lblEmail = Label(ABC2, text="Email", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblEmail.grid(row=6,column=0, sticky= W)
        self.txtEmail = Entry(ABC2, font=('Arial',12,'bold'), textvariable=Email, width=25)
        self.txtEmail.grid(row=6,column=1, pady=3, padx=20)

        self.lblN = Label(ABC2, text="Nationality", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblN.grid(row=7,column=0, sticky= W)
        self.cboN = ttk.Combobox(ABC2, font=('Arial',12,'bold'), textvariable=Nationality,
                                 state='readonly', width=23)
        self.cboN['value'] = ('', 'British', 'Nigeria', 'Korea', 'India', 'Canada', 'France', 'Norway')
        self.cboN.current(0)
        self.cboN.grid(row=7,column=1, pady=3, padx=20)

        self.lblDOB = Label(ABC2, text="Date of Birth", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblDOB.grid(row=8,column=0, sticky= W)
        self.txtDOB = Entry(ABC2, font=('Arial',12,'bold'), textvariable=DOB, width=25)
        self.txtDOB.grid(row=8,column=1, pady=3, padx=20)

        self.lblIDType = Label(ABC2, text="Type of ID", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblIDType.grid(row=9,column=0, sticky= W)
        self.cboIDType = ttk.Combobox(ABC2, font=('Arial',12,'bold'), textvariable=IDType,
                                 state='readonly', width=23)
        self.cboIDType['value'] = ('', 'Pilot Licence', 'Driving Licence', 'Student ID', 'Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1, pady=3, padx=20)

        self.lblGender = Label(ABC2, text="Gender", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblGender.grid(row=10,column=0, sticky= W)
        self.cboGender = ttk.Combobox(ABC2, font=('Arial',12,'bold'), textvariable=Gender,
                                 state='readonly', width=23)
        self.cboGender['value'] = ('', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1, pady=3, padx=20)

        self.lblCheckInDate = Label(ABC2, text="CheckInDate", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblCheckInDate.grid(row=11,column=0, sticky= W)
        self.txtCheckInDate = Entry(ABC2, font=('Arial',12,'bold'), textvariable=CheckInDate, width=25)
        self.txtCheckInDate.grid(row=11,column=1, pady=3, padx=20)

        self.lblCheckOutDate = Label(ABC2, text="CheckOutDate", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblCheckOutDate.grid(row=12,column=0, sticky= W)
        self.txtCheckOutDate = Entry(ABC2, font=('Arial',12,'bold'), textvariable=CheckOutDate, width=25)
        self.txtCheckOutDate.grid(row=12,column=1, pady=3, padx=20)

        self.lblMeal = Label(ABC2, text="Meal", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblMeal.grid(row=13,column=0, sticky= W)
        self.cboMeal = ttk.Combobox(ABC2, font=('Arial',12,'bold'), textvariable=Meal,
                                 state='readonly', width=23)
        self.cboMeal['value'] = ('', 'Breakfast', 'Lunch', 'Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1, pady=3, padx=20)

        self.lblRoomType = Label(ABC2, text="RoomType", font=('Arial',12,'bold'),
                              padx=2, pady=8, bg='Cadet blue', fg="Cornsilk")
        self.lblRoomType.grid(row=14,column=0, sticky= W)
        self.cboRoomType = ttk.Combobox(ABC2, font=('Arial',12,'bold'), textvariable=RoomType,
                                 state='readonly', width=23)
        self.cboRoomType['value'] = ('', 'Single', 'Double', 'Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1, pady=3, padx=20)

        #----------------------------------------#
        self.Latte = Checkbutton(ABC3, text="Latta ", variable=var1, onvalue=1,command=chkLatta,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,
                                        bg="powder blue").grid(row=0, sticky=W)
        self.txtLatte = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Latta, width=25, state=DISABLED)
        self.txtLatte.grid(row=0,column=1)

        self.Espresso = Checkbutton(ABC3, text="Espresso ", variable=var2, onvalue=1,command=chkEspresso,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,
                                        bg="powder blue").grid(row=1, sticky=W)
        self.txtEspresso = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Espresso, width=25, state=DISABLED)
        self.txtEspresso.grid(row=1,column=1)

        self.chkIced_Latta = Checkbutton(ABC3, text="Iced Latte ", variable=var3, onvalue=1,command=chkIced_Latta,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,
                                        bg="powder blue").grid(row=2, sticky=W)
        self.txtIced_Latta = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Iced_Latta, width=25, state=DISABLED)
        self.txtIced_Latta.grid(row=2,column=1)

        self.Vale_Coffee = Checkbutton(ABC3, text="Vale Coffee ", variable=var4, onvalue=1,command=chkVale_Coffee,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,
                                        bg="powder blue").grid(row=3, sticky=W)
        self.txtVale_Coffee = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Vale_Coffee, width=25, state=DISABLED)
        self.txtVale_Coffee.grid(row=3,column=1)

        self.Cappuccino  = Checkbutton(ABC3, text="Cappuccino ", variable=var5, onvalue=1,command=chkCappuccino,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,
                                        bg="powder blue").grid(row=4, sticky=W)
        self.txtCappuccino  = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Cappuccino, width=25, state=DISABLED)
        self.txtCappuccino.grid(row=4,column=1)

        self.African_Coffee = Checkbutton(ABC3, text="African Coffee ", variable=var6, onvalue=1,
                                          command=chkAfrican_Coffee, offvalue=0, font=('Arial',12,'bold'),
                                          pady=12, bg="powder blue").grid(row=5, sticky=W)
        self.txtAfrican_Coffee = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_African_Coffee, width=25, state=DISABLED)
        self.txtAfrican_Coffee.grid(row=5,column=1)

        self.American_Coffee = Checkbutton(ABC3, text="American Coffee", variable=var7, onvalue=1,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,command=chkAmerican_Coffee,
                                        bg="powder blue").grid(row=6, sticky=W)
        self.txtAmerican_Coffee = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_American_Coffee, width=25, state=DISABLED)
        self.txtAmerican_Coffee.grid(row=6,column=1)

        self.Iced_Cappuccino  = Checkbutton(ABC3, text="Iced Cappuccino", variable=var8, onvalue=1,
                                        offvalue=0, font=('Arial',12,'bold'), pady=12,command=chkIced_Cappuccino,
                                        bg="powder blue").grid(row=7, sticky=W)
        self.txtIced_Cappuccino  = Entry(ABC3, font=('Arial',12,'bold'), bd=8, justify='left',
                                     textvariable=E_Iced_Cappuccino, width=25, state=DISABLED)
        self.txtIced_Cappuccino.grid(row=7,column=1)

        self.lblspace = Label(ABC3, text="Tax and Total Sum",font=('Arial',12,'bold'),
                              justify=CENTER, pady=8, bd=9, bg="cadet blue",
                              fg="Cornsilk", width=40).grid(row=8, column=0, columnspan=4)

        #----------------------------------------#
        self.lblPaidTax = Label(ABC3, text="Paid Tax", font=('Arial',12,'bold'), pady=10
                              ,bg='powder blue', fg="black")
        self.lblPaidTax.grid(row=10,column=0, sticky= W)
        self.txtPaidTax = Entry(ABC3, font=('Arial',12,'bold'), textvariable=PaidTax,
                                bd=7, bg='white', width=18, justify=LEFT)
        self.txtPaidTax.grid(row=10,column=1)

        self.lblSubTotal = Label(ABC3, text="Sub Total", font=('Arial',12,'bold'),
                              bg='powder blue', fg="black")
        self.lblSubTotal.grid(row=11,column=0, sticky= W)
        self.txtSubTotal = Entry(ABC3, font=('Arial',12,'bold'), textvariable=SubTotal,
                                bd=7, bg='white', width=18, justify=LEFT)
        self.txtSubTotal.grid(row=11,column=1)

        self.lblTotalCost = Label(ABC3, text="Total Cost", font=('Arial',12,'bold'),
                             bg='powder blue', fg="black")
        self.lblTotalCost.grid(row=12,column=0, sticky= W)
        self.txtTotalCost = Entry(ABC3, font=('Arial',12,'bold'), textvariable=TotalCost,
                                bd=7, bg='white', width=18)
        self.txtTotalCost.grid(row=12,column=1)


        #--------------buttons-------------------#
        self.btnTotal = Button(ABC6, padx=8, pady=7, bd=5, text="Total", command=costOfItem,
                               font=('Arial',12,'bold'), width=5, height=2,
                               bg='powder blue', fg="black").grid(row=0, column=0)

        self.btnReset = Button(ABC6, padx=8, pady=7, bd=5, text="Reset", command=Reset,
                               font=('Arial',12,'bold'), width=5, height=2,
                               bg='powder blue', fg="black").grid(row=0, column=1)

        self.btnExit = Button(ABC6, padx=8, pady=7, bd=5, text="Exit", command=iExit,
                               font=('Arial',12,'bold'), width=5, height=2,
                               bg='powder blue', fg="black").grid(row=0, column=2)

        self.btnPrint = Button(ABC6, padx=9, pady=7, bd=5, text="Print",
                               command=lambda: sendToPrinter(str(self.txtReceipt.get("1.0", "end-1c"))),
                               font=('Arial',12,'bold'), width=5, height=2,
                               bg='powder blue', fg="black").grid(row=0, column=3)


#----------------------------------------#

if __name__ == "__main__":

    main()
