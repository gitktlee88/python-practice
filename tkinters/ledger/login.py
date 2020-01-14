
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

import ledger

class Login:
    def __init__(self, master):
        self.master = master

        # self.frame = tk.Frame(self.master, bg='powder blue')
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        font_arial = ('arial',10,'bold')
        self.Username = tk.StringVar()
        self.Password = tk.StringVar()

        self.lblTitle = tk.Label(self.frame,
                                text="Account Login System",
                                font=font_arial,
                                fg='black')
        self.lblTitle.grid(row=0, column=0,
                           columnspan=2, pady=10)

        #----------------------------------------------#
        self.LoginFrame1 = tk.LabelFrame(self.frame, width=250,
                                         height=50, bd=20,
                                         font=font_arial,
                                         relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = tk.LabelFrame(self.frame, width=250,
                                         height=50, bd=20,
                                         font=font_arial,
                                         relief='ridge')
        self.LoginFrame2.grid(row=2, column=0, pady=30)

        #----------------------------------------------#
        self.lblUsername = tk.Label(self.LoginFrame1, text='Username',
                                 font=font_arial,
                                 bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = tk.Entry(self.LoginFrame1,
                                 font=font_arial,
                                 textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, padx= 15)

        self.lblPassword = tk.Label(self.LoginFrame1,
                                 text='Password',
                                 bd=22,font=font_arial)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = tk.Entry(self.LoginFrame1,
                                 font=font_arial,
                                 textvariable=self.Password,
                                 show='*')
        self.txtPassword.grid(row=1, column=1)

        #----------------------------------------------#

        self.btnLogin = tk.Button(self.LoginFrame2, width=17,
                               font=font_arial,
                               text="Login",
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnReset = tk.Button(self.LoginFrame2, width=17,
                               font=font_arial,
                               command=self.Reset, text="Reset")
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = tk.Button(self.LoginFrame2, width=17,
                              font=font_arial,
                              command=self.iExit, text="Exit")
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

        self.txtUsername.focus_set()

        #----------------------------------------------#
    def Login_System(self):
        u = (self.Username.get())
        p = (self.Password.get())

        if (u == str(1) and p == str(1)):
            self.frame.destroy()
            # self.frame.pack_forget()
            # frameobj.pack() to show
            # frameobj.grid_forget() to hide
            # frameobj.pack_forget() to hide

            ledger.Ledger(self.master)
            # Demo2(self.master, self.master)
        else:
            tkinter.messagebox.showinfo("Login Systems",
                                        "Invalid login details")
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

class Demo2:
    def __init__(self, master, d1_master):
        self.master = master
        self.d1_master = d1_master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame,
                                    text = 'Quit',
                                    width = 25,
                                    command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()
        self.d1_master.update()
        self.d1_master.deiconify()

def main():
    root = tk.Tk()
    root.geometry("800x500")
    app = Login(root)

    root.mainloop()

if __name__ == '__main__':
    main()
