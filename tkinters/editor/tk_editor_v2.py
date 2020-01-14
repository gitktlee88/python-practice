"""
Text Editor GUI
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

import db_mysql_v2 as db

class Menubar:

    def __init__(self, parent):
        self.parent = parent

        font_specs = ("ubuntu", 12)
        font_verdi = ("Verdana", 10)

        new_file_icon = tk.PhotoImage(file='icons/new_file.png')
        open_file_icon =  tk.PhotoImage(file='icons/open_file.png')
        save_file_icon =  tk.PhotoImage(file='icons/save.png')
        cut_icon =  tk.PhotoImage(file='icons/cut.png')
        copy_icon =  tk.PhotoImage(file='icons/copy.png')
        paste_icon =  tk.PhotoImage(file='icons/paste.png')
        undo_icon =  tk.PhotoImage(file='icons/undo.png')
        redo_icon =  tk.PhotoImage(file='icons/redo.png')

        self.color_schemes = {
            'Default': '#000000.#FFFFFF',
            'Greygarious': '#83406A.#D1D4D1',
            'Aquamarine': '#5B8340.#D1E7E0',
            'Bold Beige': '#4B4620.#FFF0E1',
            'Cobalt Blue': '#ffffBB.#3333aa',
            'Olive Green': '#D1E7E0.#5B8340',
            'Night Mode': '#FFFFFF.#000000',
        }

        #---------- File menu ------------
        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_verdi, tearoff=0)
        file_dropdown.add_command(label="New File",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Open File",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Save",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Save As",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit",
                                  command=parent.master.destroy)

        # menubar.add_cascade(label='File', menu=file_dropdown)

        #---------- About menu ----------
        about_dropdown = tk.Menu(menubar, font=font_verdi, tearoff=0)
        about_dropdown.add_command(label="Release Notes",
                                   command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About",
                                   command=self.show_about_message)

        # menubar.add_cascade(label='About', menu=about_dropdown)

        #---------- Edit menu ----------
        edit_dropdown = tk.Menu(menubar, font=font_verdi, tearoff=0)
        edit_dropdown.add_command(label='Undo', accelerator='Ctrl+Z',
                              compound='left', image=undo_icon,
                              command=self.undo)
        edit_dropdown.add_command(label='Redo', accelerator='Ctrl+Y',
                              compound='left', image=redo_icon,
                              command=self.redo)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label='Cut', accelerator='Ctrl+X',
                              compound='left', image=cut_icon,
                              command=self.cut)
        edit_dropdown.add_command(label='Copy', accelerator='Ctrl+C',
                              compound='left', image=copy_icon,
                              command=self.copy)
        edit_dropdown.add_command(label='Paste', accelerator='Ctrl+V',
                              compound='left', image=paste_icon,
                              command=self.paste)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label='Find', underline=0,
                              accelerator='Ctrl+F',
                              command=self.find_text)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label='Select All', underline=7,
                              accelerator='Ctrl+A',
                              command=self.select_all)

        # menubar.add_cascade(label='Edit', menu=edit_dropdown)

        #---------- View menu --------------
        view_dropdown = tk.Menu(menubar, font=font_verdi, tearoff=0)
        self.show_line_number = tk.IntVar()
        self.show_line_number.set(1)
        view_dropdown.add_checkbutton(label='Show Line Number',
                                  variable=self.show_line_number,
                                  command=parent.update_line_numbers)
        self.show_cursor_info = tk.IntVar()
        self.show_cursor_info.set(1)
        view_dropdown.add_checkbutton(
            label='Show Cursor Location at Bottom',
            variable=self.show_cursor_info,
                command=self.parent.show_cursor_info_bar)
        self.to_highlight_line = tk.BooleanVar()
        view_dropdown.add_checkbutton(label='Highlight Current Line', onvalue=1,
                                  offvalue=0, variable=self.to_highlight_line,
                                  command=self.toggle_highlight)
        themes_dropdown = tk.Menu(menubar, font=font_verdi, tearoff=0)
        view_dropdown.add_cascade(label='Themes', menu=themes_dropdown)

        self.theme_choice = tk.StringVar()
        self.theme_choice.set('Default')
        for k in sorted(self.color_schemes):
            themes_dropdown.add_radiobutton(
                label=k, variable=self.theme_choice, command=self.change_theme)

        # menu_bar.add_cascade(label='View', menu=view_menu)

        menubar.add_cascade(label='File', menu=file_dropdown)
        menubar.add_cascade(label='Edit', menu=edit_dropdown)
        menubar.add_cascade(label='View', menu=view_dropdown)
        menubar.add_cascade(label='About', menu=about_dropdown)


        #---------- bar variables ---------
        # shortcut_bar = tk.Frame(self.parent.master,  height=25,
        #                         background='light blue')
        # shortcut_bar.pack(expand='no', fill='x')
        #
        # icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
        #          'undo', 'redo', 'find_text')
        # cmds = (self.new_file, self.open_file, self.save, self.cut,
        #          self.copy, self.paste, self.undo, self.redo, self.find_text)
        # # for i, icon in enumerate(icons):
        # for icon, cc in zip(icons, cmds):
        #     tool_bar_icon = tk.PhotoImage(file='icons/{}.png'.format(icon))
        #
        #     """
        #     #-- eval() evaluates the passed string as a Python expression
        #     #-- and returns the result.
        #     #-- For example, eval("1 + 1") interprets and executes the
        #     #-- expression "1 + 1" and returns the result (2).
        #     """
        #     # cmd = eval(icon)
        #     tool_bar = tk.Button(shortcut_bar, image=tool_bar_icon, command=cc)
        #     tool_bar.image = tool_bar_icon
        #     tool_bar.pack(side='left')
        #
        # self.line_number_bar = tk.Text(menubar, width=3, padx=3, takefocus=0,
        #                           border=0, background='light blue',
        #                           state='disabled',  wrap='none')
        # self.line_number_bar.pack(side='left',  fill='y')

        #---------- variables from MainWindow ---------
        self.content_text = self.parent.content_text
        # self.cursor_info_bar = self.parent.cursor_info_bar
        # self.show_cursor_info_bar = self.parent.show_cursor_info_bar






        #---------- File menu handler---------
    def show_about_message(self):
        box_title = "About PyText"
        box_message = "A simple Python Text Editor"
        messagebox.showinfo(box_title, box_message)

    def show_release_notes(self):
        box_title = "Release Notes"
        box_message = "Version 0.1 - Gutenberg"
        messagebox.showinfo(box_title, box_message)

        #-------- Edit menu handler ------------
    def cut(self):
        self.content_text.event_generate("<<Cut>>")
        self.parent.on_content_changed()
        return "break"

    def copy(self):
        self.content_text.event_generate("<<Copy>>")
        return "break"

    def paste(self):
        self.content_text.event_generate("<<Paste>>")
        self.parent.on_content_changed()
        return "break"

    def undo(self):
        self.content_text.event_generate("<<Undo>>")
        self.parent.on_content_changed()
        return "break"

    def redo(self, event=None):
        self.content_text.event_generate("<<Redo>>")
        self.parent.on_content_changed()
        return 'break'

        #-------- content area handler ------------
    def show_popup_menu(self, event):
        popup_menu.tk_popup(event.x_root, event.y_root)

    def change_theme(self, event=None):
        selected_theme = self.theme_choice.get()
        fg_bg_colors = self.color_schemes.get(selected_theme)
        foreground_color, background_color = fg_bg_colors.split('.')
        self.content_text.config(
            background=background_color, fg=foreground_color)

    def highlight_line(self, interval=100):
        self.content_text.tag_remove("active_line", 1.0, "end")
        self.content_text.tag_add(
            "active_line", "insert linestart", "insert lineend+1c")
        self.content_text.after(interval, self.toggle_highlight)

    def undo_highlight(self):
        self.content_text.tag_remove("active_line", 1.0, "end")

    def toggle_highlight(self, event=None):
        if self.to_highlight_line.get():
            self.highlight_line()
        else:
            self.undo_highlight()

    def select_all(self, event=None):
        self.content_text.tag_add('sel', '1.0', 'end')
        return "break"

    def find_text(self, event=None):
        search_toplevel = tk.Toplevel(self.parent.master)
        search_toplevel.title('Find Text')
        search_toplevel.transient(self.parent.master)

        tk.Label(search_toplevel, text="Find All:").grid(
                                    row=0, column=0, sticky='e')

        search_entry_widget = tk.Entry(
            search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1,
                                 padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        ignore_case_value = tk.IntVar()
        tk.Checkbutton(search_toplevel, text='Ignore Case',
                    variable=ignore_case_value).grid(
                    row=1, column=1, sticky='e', padx=2, pady=2)

        # Calling a Method(Callback) When the Button is Pressed
        tk.Button(search_toplevel, text="Find All", underline=0,
               command=lambda: self.search_output(
                   search_entry_widget.get(),
                   ignore_case_value.get(),
                   self.content_text,
                   search_toplevel,
                   search_entry_widget)
               ).grid(row=0, column=2, sticky='e' + 'w',
                      padx=2, pady=2)

    def search_output(self, needle, if_ignore_case, content_text,
                      search_toplevel, search_box):
        content_text.tag_remove('match', '1.0', tk.END)
        matches_found = 0
        if needle:
            start_pos = '1.0'
            while True:
                start_pos = content_text.search(needle, start_pos,
                                        nocase=if_ignore_case,
                                        stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(needle))
                content_text.tag_add('match', start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos
                content_text.tag_config(
                'match', foreground='red', background='yellow')
        search_box.focus_set()
        search_toplevel.title('{} matches found'.format(matches_found))

        #-------- Edit menu handler ------------



class Statusbar:

    def __init__(self, parent):

        font_specs = ("Verdana", 10, "italic")

        self.status = tk.StringVar()
        self.status.set("PyText - 0.1 Gutenberg")

        self.label = tk.Label(parent.content_text, textvariable=self.status,
                         fg="black", bg="lightgrey", anchor='sw',
                         font=font_specs)
        self.label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        self.label.config(fg='black')
        # if isinstance(args[0], bool):
        if args[0] == 1:
            self.status.set("Your File Has Been Saved!")
        elif args[0] == 2:
            self.status.set("DB Update Has Been Completed!")
        elif args[0] == 3:
            self.status.set("Wait, Selection First!")
            self.label.config(fg='red')
        else:
            self.status.set("PyText - 0.1 Cool")

class Sidebar:

    def __init__(self, parent):

        font_specs = ("Verdana", 10, "italic")
        font_gulim = ("GulimChe", 10, "italic")

        self.parent = parent
        # self.mydb = db.MySQLdb_connection()

        self.view_command()

        self.parent.list_box.bind('<<ListboxSelect>>',
                           self.get_selected_row)

        #----------------------------------
        self.show_line_number = tk.IntVar()
        self.show_line_number.set(1)
        self.show_cursor_info = tk.IntVar()
        self.show_cursor_info.set(1)
        self.title_info = tk.StringVar()   #temp
        self.title_info.set('')          #temp

    def view_command(self):
        self.parent.list_box.delete(0,tk.END)

        sql = "SELECT word FROM mydic.words ORDER BY `word`"
        titles = self.parent.mydb.query_db(sql, db_use = 'mydic')
        # print(titles)
        for row in titles:
            self.parent.list_box.insert(tk.END,row[0])
            # print(row)
    def query_command(self, sql):
        results = self.parent.mydb.query_db(sql, db_use = 'mydic')

        return results

    def get_selected_row(self, event):
        try:
            # index = self.parent.list_box.curselection()[0]
            index = self.parent.list_box.curselection()
            word = self.parent.list_box.get(index)
            self.parent.statusbar.update_status('x')
            self.title_info.set(word) #temp

            r = self.query_command("SELECT descr FROM mydic.words WHERE word = '%s' " % word)
            # import pdb
            # pdb.set_trace()

            # MainTextBox.delete(0, END)
            # OutputBox.delete('1.0', END)
            self.parent.content_text.delete('1.0', tk.END)
            # self.parent.content_text.insert(tk.END, r[0][0])
            self.parent.content_text.insert(tk.END, r[0][0])
        except Exception as e:
            # print(e)
            return

class MainWindow:

    def __init__(self, master):
        master.title("Untitled - PyText Editor")

        font_specs = ("ubuntu", 10, 'italic')
        font_verdi = ("Verdana", 8)
        font_gulim = ("GulimChe", 8)

        self.master = master
        self.filename = None
        self.mydb = db.MySQLdb_connection()
        # from tkinter import font
        # print(font.families())

        # Create Frame widget --------------------------
        left_frame = tk.Frame(master, width=500, height=450)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        right_frame = tk.Frame(master, width=150, height=450, bg='light blue')
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Create  Content Textarea & Scroll bar on left_frame -------
        self.line_number_bar = tk.Text(left_frame, width=3, padx=3,
                                    takefocus=0, border=0,
                                    background='light blue',
                                    state='disabled',  wrap='none')
        self.line_number_bar.pack(side='left',  fill='y')

        scroll_bar = tk.Scrollbar(left_frame)
        self.content_text = tk.Text(left_frame, wrap='word',
                                    font=font_specs, undo=1,
                                    yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.content_text.yview)
        scroll_bar.pack(side='right', fill='y')
        self.content_text.pack(expand='yes', fill='both')

        # scroll_bar = tk.Scrollbar(self.content_text)
        # self.content_text.configure(yscrollcommand=scroll_bar.set)


        self.cursor_info_bar = tk.Label(self.content_text,
                                        text='Line: 1 | Column: 1')
        self.cursor_info_bar.pack(expand='no', fill=None,
                                  side='right', anchor='se')

        # Create  Listbox & Scroll bar on rightt_frame ------
        scroll_bar2 = tk.Scrollbar(right_frame)
        self.list_box = tk.Listbox(right_frame,width=25,
                                   font=font_verdi,
                                   yscrollcommand=scroll_bar2.set)
        scroll_bar2.config(command=self.list_box.yview)
        scroll_bar2.pack(side='right', fill='both')
        self.list_box.pack(side='left', expand=True, fill='both')

        #-------------  binds events-------------------------
        self.content_text.bind('<Any-KeyPress>', self.on_content_changed)
        self.content_text.tag_configure('active_line', background='ivory2')

        # Instance of Menubar & Statusbar -----
        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        self.sidebar = Sidebar(self)

        self.bind_shortcuts()


        """
        #-- eval() evaluates the passed string as a Python expression
        #-- and returns the result.
        #-- For example, eval("1 + 1") interprets and executes the
        #-- expression "1 + 1" and returns the result (2).
        """
        # set up the pop-up menu
        self.popup_menu = tk.Menu(self.content_text, tearoff=0)

        # for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
        for i in ('self.save', 'self.save_as', 'self.update_db',
                  'self.insert_db', 'self.delete_db'):
            cmd = eval(i)
            self.popup_menu.add_command(label=i, compound='left', command=cmd)

        self.popup_menu.add_separator()
        self.popup_menu.add_command(label='Select All', underline=7,
                               command=self.select_all)
        self.content_text.bind('<Button-3>', self.show_popup_menu)


        # bind right mouse click to show pop up and set focus to text widget on launch
        self.content_text.bind('<Button-3>', self.show_popup_menu)
        self.content_text.focus_set()





    # show pop-up menu
    def show_popup_menu(self, event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)
        # print(self.sidebar.title_info.get())

    def select_all(self, event=None):
        self.content_text.tag_add('sel', '1.0', 'end')
        return "break"

    #---------  Handlers ------------
    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Untitled - PyText")

    def new_file(self, *args):
        self.content_text.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.content_text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.content_text.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.content_text.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                # self.statusbar.update_status(True)
                self.statusbar.update_status(1)
            except Exception as e:
                # print(e)
                pass
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css")])
            textarea_content = self.content_text.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            # print(e)
            pass

    def delete_db(self, *args):
        title = self.sidebar.title_info.get()
        # mydb = db.MySQLdb_connection()
        if title and tk.messagebox.askokcancel("Sure to DELETE the WORD from the DATABASE?",'"'+title+'"'):
            sql = "DELETE FROM mydic.words WHERE word = '%s'" % (title)
            results = self.mydb.query_db(sql, db_use = 'mydic')
            self.content_text.delete('1.0', tk.END)
            self.sidebar.title_info.set('')
            self.statusbar.update_status(2)
            self.sidebar.view_command()

        else:
            self.statusbar.update_status(3)

    def update_db(self, *args):
        title = self.sidebar.title_info.get()
        textarea_content = self.content_text.get(1.0, tk.END)
        # mydb = db.MySQLdb_connection()

        if title:
            sql = "UPDATE mydic.words SET descr = '%s' WHERE word = '%s'" % (textarea_content, title)

            results = self.mydb.query_db(sql, db_use = 'mydic')
            self.content_text.delete('1.0', tk.END)
            self.sidebar.title_info.set('')
            self.statusbar.update_status(2)

        else:
            self.statusbar.update_status(3)

    def insert_db(self, *args):
        title = simpledialog.askstring(title="Word",
                                  prompt="Insert Word As What Name?:")
        # title = self.sidebar.title_info.get()
        textarea_content = self.content_text.get(1.0, tk.END)
        # mydb = db.MySQLdb_connection()

        if title:
            sql = "INSERT INTO mydic.words (word, descr) VALUES ('%s', '%s')" % (title, textarea_content)
            results = self.mydb.query_db(sql, db_use = 'mydic')
            self.content_text.delete('1.0', tk.END)
            self.sidebar.title_info.set('')
            self.statusbar.update_status(2)
            self.sidebar.view_command()

        else:
            self.statusbar.update_status(4)


    #---------------------------------------
    def show_cursor_info_bar(self):
        show_cursor_info_checked = self.menubar.show_cursor_info.get()
        if show_cursor_info_checked:
            self.cursor_info_bar.pack(expand='no', fill=None,
                                      side='right', anchor='se')
        else:
            self.cursor_info_bar.pack_forget()

    def update_cursor_info_bar(self, event=None):
        row, col = self.content_text.index(tk.INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        self.cursor_info_bar.config(text=infotext)

    def get_line_numbers(self):
        output = ''
        if self.menubar.show_line_number.get():
            row, col = self.content_text.index("end").split('.')
            for i in range(1, int(row)):
                output += str(i) + '\n'
        return output

    def on_content_changed(self, event=None):
        self.update_line_numbers()
        self.update_cursor_info_bar()

    def update_line_numbers(self, event=None):
        line_numbers = self.get_line_numbers()
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete('1.0', 'end')
        self.line_number_bar.insert('1.0', line_numbers)
        self.line_number_bar.config(state='disabled')

    def bind_shortcuts(self):
        self.content_text.bind('<Control-n>', self.new_file)
        self.content_text.bind('<Control-o>', self.open_file)
        self.content_text.bind('<Control-s>', self.save)
        self.content_text.bind('<Control-S>', self.save_as)
        self.content_text.bind('<Key>', self.statusbar.update_status)
        self.content_text.bind('<Any-KeyPress>', self.on_content_changed)



if __name__ == "__main__":
    master = tk.Tk()
    master.geometry("800x500")
    app = MainWindow(master)
    master.mainloop()
