import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
# import ast, json

### In case you are using Virtualenv on Windows I found a solution.
### I copied the "tcl" folder from C:\Python27\ over to
### the root of the Virtualenv.

# import ledger_bk
import db_mongo

class Ledger:

    def __init__(self, master):
        global dm
        self.master = master
        userinfo = {
            'user':'mongo88',
            'pw':'kclkt88',
            'dbname':'business',
            'coll':'ledgerdata'
            }

        dm = db_mongo.Mongodb_atlas_conn(**userinfo)
        # window = Tk()
        # window.title("Account Management")
        master.title("Account Management")

        self.l1 = tk.Label(self.master,text="Name")
        self.l1.grid(row=0,column=0,columnspan=2)
        self.l2 = tk.Label(self.master,text="Username/Email")
        self.l2.grid(row=1,column=0,columnspan=2)
        self.l3 = tk.Label(self.master,text="Password")
        self.l3.grid(row=2,column=0,columnspan=2)
        self.l4 = tk.Label(self.master,text="Category")
        self.l4.grid(row=3,column=0,columnspan=2)
        self.l5 = tk.Label(self.master,text="Date")
        self.l5.grid(row=4,column=0,columnspan=2)
        # self.l6 = tk.Label(self.master,text="Id")
        # self.l6.grid(row=5,column=0,columnspan=2)

        self.name = tk.StringVar()
        self.e1 = tk.Entry(self.master,textvariable=self.name,width=50)
        self.e1.grid(row=0,column=0,columnspan=10)

        self.user = tk.StringVar()
        self.e2 = tk.Entry(self.master,textvariable=self.user,width=50)
        self.e2.grid(row=1,column=0,columnspan=10)

        self.password = tk.StringVar()
        self.e3 = tk.Entry(self.master,textvariable=self.password,width=50)
        self.e3.grid(row=2,column=0,columnspan=10)

        self.category = tk.StringVar()
        self.e4 = tk.Entry(self.master,textvariable=self.category,width=50)
        self.e4.grid(row=3,column=0,columnspan=10)

        self.cdate=tk.StringVar()
        self.e5 = tk.Entry(self.master,textvariable=self.cdate,width=50)
        self.e5.grid(row=4,column=0,columnspan=10)

        # self.id=tk.StringVar()
        # self.e6 = tk.Entry(self.master,textvariable=self.id,width=50)
        # self.e6.grid(row=5,column=0,columnspan=10)
        # self.e6.config(state=DISABLED)

        self.b1 = tk.Button(self.master,text="Add",width=12,
                            command=self.add_command)
        self.b1.grid(row=6,column=0)

        self.b2 = tk.Button(self.master,text="Update",width=12,
                            command=self.update_command)
        self.b2.grid(row=6,column=1)

        self.b3 = tk.Button(self.master,text="Search",width=12,
                            command=self.search_command)
        self.b3.grid(row=6,column=2)

        self.b4 = tk.Button(self.master,text="View All",width=12,
                            command=self.view_command)
        self.b4.grid(row=6,column=3)

        self.b5 = tk.Button(self.master,text="Delete",width=12,
                            command=self.delete_command)
        self.b5.grid(row=6,column=4)

        self.b6 = tk.Button(self.master,text="Cancel",width=12,
                            command=self.master.destroy)
        self.b6.grid(row=6,column=5)

        self.b7 = tk.Button(self.master,text="Clear All",width=12,
                            command=self.clear_command)
        self.b7.grid(row=0,column=5)

        self.lb = tk.Listbox(self.master,height=20,width=94)
        self.lb.grid(row=7,column=0,columnspan=6)

        self.sb = tk.Scrollbar(self.master, orient=tk.VERTICAL)
        self.sb.grid(row=7,column=6, sticky=tk.N + tk.S + tk.E)

        self.lb.configure(yscrollcommand=self.sb.set)
        self.sb.configure(command=self.lb.yview)
        #------- bind -------
        self.lb.bind('<<ListboxSelect>>',self.get_selected_row)

    def view_command(self):
        self.lb.delete(0,tk.END)
        # for row in ledger_bk.viewall():
        i = 1
        lst = [i]

        for row in dm.find_all_docs():
            # del row['_id']
            row.pop('_id')

            lv = [v for k, v in row.items()]
            lst += lv

            self.lb.insert(tk.END, tuple(lst))
            i += 1
            lst = [i]

    def search_command(self):
        self.lb.delete(0,tk.END)

        # for row in ledger_bk.search(name=self.name.get(),\
        lst = dm.find_one_doc(name=self.name.get(),\
                                user=self.user.get(),\
                                password=self.password.get(),\
                                category=self.category.get())
            # row.pop('_id')
            # lv = [v for k, v in row.items()]
            # lst += lv

        self.lb.insert(tk.END,tuple(lst))

    def add_command(self):
        # ledger_bk.add(self.name.get(),self.user.get(),\
        dm.insert_one_doc(self.name.get(),self.user.get(),\
                  self.password.get(),self.category.get(),self.cdate.get())
        self.lb.delete(0,tk.END)
        self.lb.insert(tk.END,self.name.get(),self.user.get(),\
                  self.password.get(),self.category.get(),self.cdate.get())

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lb.curselection()[0]
            selected_tuple = self.lb.get(index)

            # s = ast.literal_eval("('%s',)" % selected_tuple)
            # print(s)

            self.e1.delete(0,tk.END)
            self.e1.insert(tk.END,selected_tuple[1])
            self.e2.delete(0,tk.END)
            self.e2.insert(tk.END,selected_tuple[2])
            self.e3.delete(0,tk.END)
            self.e3.insert(tk.END,selected_tuple[3])
            self.e4.delete(0,tk.END)
            self.e4.insert(tk.END,selected_tuple[4])
            self.e5.delete(0,tk.END)
            self.e5.insert(tk.END,selected_tuple[5])
        except IndexError:
            pass

    def update_command(self):
        # ledger_bk.update(selected_tuple[0],self.name.get(),\
        dm.update_one_doc(self.name.get(),\
                         self.user.get(),self.password.get(),\
                         self.category.get(),self.cdate.get())
        self.view_command()

    def delete_command(self):
        # ledger_bk.delete(selected_tuple[0])
        dm.delete_one_doc(selected_tuple[0])
        self.view_command()
        #lb.delete(tk.END,get_selected_row.selected_tuple)
    def clear_command(self):
        self.lb.delete(0,tk.END)
        self.e1.delete(0,tk.END)
        self.e2.delete(0,tk.END)
        self.e3.delete(0,tk.END)
        self.e4.delete(0,tk.END)
        self.e5.delete(0,tk.END)

    # def __repr__(self, str):
    #     # Allow str.__repr__() to do the hard work, then
    #     # remove the outer two characters, single quotes,
    #     # and replace them with double quotes.
    #     return ''.join(('"', super().__repr__()[1:-1], '"'))

# window.mainloop()

# if __name__ == "__main__":
    # self.master.mainloop()
