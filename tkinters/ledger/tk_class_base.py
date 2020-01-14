"""
The important things to notice are:
- don't use a wildcard import.
  import the package as "tk", which requires that I prefix
  all commands with tk.
  This prevents global namespace pollution, plus it makes
  the code completely obvious when you are using
  Tkinter classes, ttk classes, or some of your own.

- The main application is a class.
  This gives you a private namespace for all of
  your callbacks and private functions, and just generally
  makes it easier to organize your code.

- If your app has additional toplevel windows,
  I recommend making each of those a separate class,
  inheriting from tk.Toplevel.
  Putting each of top-level windows into it's own separate class
  gives you code re-use and better code organization.
  Any buttons and relevant methods that are present in the window
  should be defined inside this class.
"""

import tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame,
                                 text = 'New Window',
                                 width = 25,
                                 command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        
    def new_window(self):
        self.master.withdraw()
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, self.master)

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
    # root.geometry("800x600")
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
