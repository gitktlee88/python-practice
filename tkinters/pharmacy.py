"""
Pharmacy Management System
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time;
import datetime

# import db_mysql as db

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title('Pharmacy Management System')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        font_specs = ("ubuntu", 50)
        font_arial = ("arial", 16, 'bold')
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text='Pharmacy Management',
                              font=font_specs)
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        #--------------- Frames -----------
        self.Loginframe1 = Frame(self.frame, width=1010, height=300,
                                 bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.lbl_text = Label(self.frame)
        self.lbl_text.grid(row=2, columnspan=2)

        self.Loginframe2 = Frame(self.frame, width=1010, height=100,
                                 bd=20, relief='ridge')
        self.Loginframe2.grid(row=3, column=0)

        self.Loginframe3 = Frame(self.frame, width=1010, height=200,
                                 bd=20, padx=6, pady=2, relief='ridge')
        self.Loginframe3.grid(row=4, column=0)

        #---------------          -----------
        self.lblUsername = Label(self.Loginframe1, text='Username',
                              font=font_arial, bd=20)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1,
                              textvariable=self.Username,
                              font=font_arial, bd=20)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.Loginframe1, text='Password',
                              font=font_arial, bd=20)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, show='*',
                              textvariable=self.Password,
                              font=font_arial, bd=20)
        self.txtPassword.grid(row=1, column=1)




        #--------------- Buttons for Loginframe2 -----------
        self.btnLogin = Button(self.Loginframe2,font=font_arial,
                                 text='Login', width=15,
                                 command=self.login_system)
        self.btnLogin.grid(row=0, column=0, padx=4)
        self.btnLogin.bind('<Return>', self.login_system)

        self.btnReset = Button(self.Loginframe2,font=font_arial,
                                 text='Reset', width=15,
                                 command=self.reset)
        self.btnReset.grid(row=0, column=1, padx=4)

        self.btnExit = Button(self.Loginframe2,font=font_arial,
                                 text='Exit', width=15,
                                 command=self.iExit)
        self.btnExit.grid(row=0, column=2, padx=4)

        #--------------- Buttons for Loginframe3 -----------
        self.btnRegistration = Button(self.Loginframe3, padx=14,
                                 text='Patients Registration System',
                                 state=DISABLED, font=('arial',14,'bold'),
                                 command=self.register_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, padx=14,
                                 text='Hospital Management System',
                                 state=DISABLED, font=('arial',14,'bold'),
                                 command=self.hospital_window)
        self.btnHospital.grid(row=0, column=1)

        self.txtUsername.focus_set()



    def register_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def login_system(self):
        try:
            u = (self.Username.get())
            p = (self.Password.get())
        except:
            self.lbl_text.config(text="username, password required",
                                 fg='red')
            return

        if (u == str(1) and p == str(1)):
            # self.frame.destroy()
            # # self.frame.pack_forget()
            # # frameobj.pack() to show
            # # frameobj.grid_forget() to hide
            # # frameobj.pack_forget() to hide
            self.btnRegistration.config(state=NORMAL, fg='blue')
            self.btnHospital.config(state=NORMAL, fg='blue')
        else:
            self.lbl_text.config(text="username, password required",
                                 fg='red')
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
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


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title('Patients Registration System')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        font_specs = ("ubuntu", 50)
        font_arial = ("arial", 16, 'bold')
        #=================================
        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()

        Membership=StringVar()
        Membership.set("0")

        #================================
        def iExit():
            self.master.destroy()
            return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMembership.config(state=DISABLED)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel(
                "Patiens Registration Systems", "Please Confirm 'OK'"
            )
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0", END)

        def Ref_No():
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t"+Ref.get()+"\t\t"+Firstname.get() \
                                   +"\t\t"+Surname.get()+"\t\t"+Address.get() \
                                   +"\t\t"+DateofOrder.get()+"\t\t"+Telephone.get() \
                                   +"\t\t"+Membership.get()+"\n"
                                   )
        def Membership_Fees():
            if(var4.get() == 1):
                self.txtMembership.configure(state=NORMAL)
                item1 = float(50)
                Membership.set("$" + str(Item1))
            elif (var4.get() == 0):
                elf.txtMembership.configure(state=DISABLED)
                Membership.set("0")

        #================================
        #================================
        #================================

        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, bd=20, width=1350, padx=53,
                           relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame,
                              text='Patients Registration System',
                              font=('ubunto',59,'bold'), padx=49)
        self.lblTitle.grid()

        #========= LowerFrames ==========
        MemberDetailsFrame = LabelFrame(Mainframe, bd=20, pady=5,
                                width=1350, height=500, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, pady=2,
                                  width=880, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, pady=3,
                                   font=('arial',12,'bold'),
                                   text='Customer Name',
                                   width=350, height=400, relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10,
                                    width=800, height=400, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
        #================================
        self.lblReferenceNo = Label(MembersName_F, text='Reference No',
                              font=('arial',14,'bold'), bd=7)
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F,textvariable=Ref,
                        font=('arial',14,'bold'), bd=7,
                        state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstname = Label(MembersName_F, text='Firstname',
                              font=('arial',14,'bold'), bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(MembersName_F,textvariable=Firstname,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(MembersName_F, text='Surname',
                              font=('arial',14,'bold'), bd=7)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(MembersName_F,textvariable=Surname,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtSurname.grid(row=2, column=1)

        self.lblAddress = Label(MembersName_F, text='Address',
                              font=('arial',14,'bold'), bd=7)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(MembersName_F,textvariable=Address,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtAddress.grid(row=3, column=1)

        self.lblPostCode = Label(MembersName_F, text='PostCode',
                              font=('arial',14,'bold'), bd=7)
        self.lblPostCode.grid(row=4, column=0, sticky=W)
        self.txtPostCode = Entry(MembersName_F,textvariable=Postcode,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtPostCode.grid(row=4, column=1)

        self.lblTelephone = Label(MembersName_F, text='Telephone',
                              font=('arial',14,'bold'), bd=7)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.txtTelephone = Entry(MembersName_F,textvariable=Telephone,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtTelephone.grid(row=5, column=1)


        self.lblDate = Label(MembersName_F, text='Date',
                              font=('arial',14,'bold'), bd=7)
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.txtDate = Entry(MembersName_F,textvariable=DateofOrder,
                        font=('arial',14,'bold'), bd=7, insertwidth=2)
        self.txtDate.grid(row=6, column=1)
        #================================
        self.lblProve_of_ID = Label(MembersName_F, bd=7,
                font=('arial',14,'bold'),text="Prove of ID")
        self.lblProve_of_ID.grid(row=7, column=0, sticky=W)

        self.cboProve_of_ID = ttk.Combobox(MembersName_F,
                font=('arial',14,'bold'),textvariable=var1,
                state='readonly', width=19)
        self.cboProve_of_ID['value'] = ('', 'Pilot Licence',
                                     'Passport', 'Driving Licence')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_of_Member = Label(MembersName_F, bd=7,
                font=('arial',14,'bold'),text="Type of Member")
        self.lblType_of_Member.grid(row=8, column=0, sticky=W)

        self.cboType_of_Member = ttk.Combobox(MembersName_F,
                font=('arial',14,'bold'),textvariable=var2,
                state='readonly', width=19)
        self.cboType_of_Member['value'] = ('', 'A','B', 'C')
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(MembersName_F, bd=7,
                font=('arial',14,'bold'),text="Method of Payment")
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F,
                font=('arial',14,'bold'),textvariable=var3,
                state='readonly', width=19)
        self.cboMethod_of_Payment['value'] = ('', 'Debit','Cash', 'Free')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        #================================
        self.chkMembership = Checkbutton(MembersName_F,
                text="Patient Fees", variable=var4, onvalue=1,
                offvalue=0, font=('arial',16,'bold'),
                command=Membership_Fees).grid(row=10, column=0)
        self.txtMembership = Entry(MembersName_F, bd=7,
                font=('arial',14,'bold'),insertwidth=2,
                state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10, column=1)
        #================================
        self.lblLabel = Label(Receipt_ButtonFrame, bd=10,
                text='Patient Ref\t Firstname\t Aurname\t Address\t \
                Date Reg.\t Telephone\t Patient Paid',
                font=('arial',10,'bold'))
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame, width=112,
                               height=22, bd=10,
                               font=('arial',10,'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)
        #================================
        self.btnReceipt = Button(Receipt_ButtonFrame,font=('arial',16,'bold'),
                                 text='Receipt', width=13, bd=7,padx=18,
                                 command=Receipt).grid(row=2, column=0)
        self.btnReset = Button(Receipt_ButtonFrame,font=('arial',16,'bold'),
                                 text='Reset', width=13, bd=7,padx=18,
                                 command=Reset).grid(row=2, column=1)
        self.btnExit = Button(Receipt_ButtonFrame,font=('arial',16,'bold'),
                                 text='Exit', width=13, bd=7,padx=18,
                                 command=iExit).grid(row=2, column=2)
        #================================
    #     self.quitButton = Button(self.frame, text='Quit',
    #                              width=25, command=self.iExit)
    #     self.quitButton.grid(row=3, column=0)
    #
    # def iExit(self):

        #=================================

class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital Management System')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        font_specs = ("ubuntu", 12)
        font_arial = ("arial", 20, 'bold')
        #=================================



        #=================================




def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
