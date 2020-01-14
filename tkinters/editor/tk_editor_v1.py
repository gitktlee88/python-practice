import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

PROGRAM_NAME = "Text Editor GUI"
file_name = None

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        # self.button1 = tk.Button(self.frame,
        #                          text = 'New Window',
        #                          width = 85, height=30,
        #                          command = self.new_window)
        # self.button1.pack()
        # self.frame.pack()

        self.menubar = Menubar(self)


    def new_window(self):
        # self.master.withdraw()
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

class Menubar:
    def __init__(self, parent):
        self.parent = parent
        font_specs = ('Arial',14,'bold')

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

        menu_bar = tk.Menu(self.parent.master, font=font_specs)
        self.parent.master.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='New', accelerator='Ctrl+N',
                              compound='left',
                              image=new_file_icon, underline=0,
                              command=self.new_file)
        file_menu.add_command(label='Open', accelerator='Ctrl+O',
                              compound='left',
                              image=open_file_icon, underline=0,
                              command=self.open_file)
        file_menu.add_command(label='Save', accelerator='Ctrl+S',
                              compound='left', image=save_file_icon,
                              underline=0, command=self.save)
        file_menu.add_command(
                        label='Save as', accelerator='Shift+Ctrl+S',
                        command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', accelerator='Alt+F4',
                              command=self.exit_editor)
        menu_bar.add_cascade(label='File', menu=file_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label='Undo', accelerator='Ctrl+Z',
                              compound='left', image=undo_icon,
                              command=self.undo)
        edit_menu.add_command(label='Redo', accelerator='Ctrl+Y',
                              compound='left', image=redo_icon,
                              command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label='Cut', accelerator='Ctrl+X',
                              compound='left', image=cut_icon,
                              command=self.cut)
        edit_menu.add_command(label='Copy', accelerator='Ctrl+C',
                              compound='left', image=copy_icon,
                              command=self.copy)
        edit_menu.add_command(label='Paste', accelerator='Ctrl+V',
                              compound='left', image=paste_icon,
                              command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label='Find', underline=0,
                              accelerator='Ctrl+F',
                              command=self.find_text)
        edit_menu.add_separator()
        edit_menu.add_command(label='Select All', underline=7,
                              accelerator='Ctrl+A',
                              command=self.select_all)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)


        view_menu = tk.Menu(menu_bar, tearoff=0)
        self.show_line_number = tk.IntVar()
        self.show_line_number.set(1)
        view_menu.add_checkbutton(label='Show Line Number',
                                  variable=self.show_line_number,
                                  command=self.update_line_numbers)
        self.show_cursor_info = tk.IntVar()
        self.show_cursor_info.set(1)
        view_menu.add_checkbutton(
            label='Show Cursor Location at Bottom',
            variable=self.show_cursor_info,
                command=self.show_cursor_info_bar)
        self.to_highlight_line = tk.BooleanVar()
        view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                                  offvalue=0, variable=self.to_highlight_line,
                                  command=self.toggle_highlight)
        self.themes_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_cascade(label='Themes', menu=self.themes_menu)

        self.theme_choice = tk.StringVar()
        self.theme_choice.set('Default')
        for k in sorted(self.color_schemes):
            self.themes_menu.add_radiobutton(
                label=k, variable=self.theme_choice, command=self.change_theme)
        menu_bar.add_cascade(label='View', menu=view_menu)

        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='About',
                               command=self.display_about_messagebox)
        about_menu.add_command(label='Help',
                               command=self.display_help_messagebox)
        menu_bar.add_cascade(label='About',  menu=about_menu)
        # self.parent.master.config(menu=menu_bar)

        shortcut_bar = tk.Frame(self.parent.master,  height=25,
                                background='light blue')
        shortcut_bar.pack(expand='no', fill='x')

        icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
                 'undo', 'redo', 'find_text')
        cmds = (self.new_file, self.open_file, self.save, self.cut,
                 self.copy, self.paste, self.undo, self.redo, self.find_text)
        # for i, icon in enumerate(icons):
        for icon, cc in zip(icons, cmds):
            tool_bar_icon = tk.PhotoImage(file='icons/{}.png'.format(icon))

            """
            #-- eval() evaluates the passed string as a Python expression
            #-- and returns the result.
            #-- For example, eval("1 + 1") interprets and executes the
            #-- expression "1 + 1" and returns the result (2).
            """
            # cmd = eval(icon)
            tool_bar = tk.Button(shortcut_bar, image=tool_bar_icon, command=cc)
            tool_bar.image = tool_bar_icon
            tool_bar.pack(side='left')

        self.line_number_bar = tk.Text(self.parent.master, width=3, padx=3, takefocus=0,
                                  border=0, background='light blue',
                                  state='disabled',  wrap='none')
        self.line_number_bar.pack(side='left',  fill='y')

        self.content_text = tk.Text(self.parent.master, wrap='word', undo=1)
        self.content_text.pack(expand='yes', fill='both')
        scroll_bar = tk.Scrollbar(self.content_text)
        self.content_text.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.content_text.yview)
        scroll_bar.pack(side='right', fill='y')
        self.cursor_info_bar = tk.Label(self.content_text, text='Line: 1 | Column: 1')
        self.cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


        self.content_text.bind('<KeyPress-F1>', self.display_help_messagebox)
        self.content_text.bind('<Control-N>', self.new_file)
        self.content_text.bind('<Control-n>', self.new_file)
        self.content_text.bind('<Control-O>', self.open_file)
        self.content_text.bind('<Control-o>', self.open_file)
        self.content_text.bind('<Control-S>', self.save)
        self.content_text.bind('<Control-s>', self.save)
        self.content_text.bind('<Control-f>', self.find_text)
        self.content_text.bind('<Control-F>', self.find_text)
        self.content_text.bind('<Control-A>', self.select_all)
        self.content_text.bind('<Control-a>', self.select_all)
        self.content_text.bind('<Control-y>', self.redo)
        self.content_text.bind('<Control-Y>', self.redo)
        self.content_text.bind('<Any-KeyPress>', self.on_content_changed)
        self.content_text.tag_configure('active_line', background='ivory2')

        # set up the pop-up menu
        popup_menu = tk.Menu(self.content_text)
        # for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
        for i in (self.cut, self.copy, self.paste, self.undo, self.redo):
            # cmd = eval(i)
            popup_menu.add_command(label=i, compound='left', command=i)
        popup_menu.add_separator()
        popup_menu.add_command(label='Select All', underline=7,
                               command=self.select_all)
        self.content_text.bind('<Button-3>', self.show_popup_menu)


        # bind right mouse click to show pop up and set focus to text widget on launch
        self.content_text.bind('<Button-3>', self.show_popup_menu)
        self.content_text.focus_set()

    # show pop-up menu
    def show_popup_menu(self, event):
        popup_menu.tk_popup(event.x_root, event.y_root)

    def show_cursor_info_bar(self):
        show_cursor_info_checked = self.show_cursor_info.get()
        if show_cursor_info_checked:
            self.cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
        else:
            self.cursor_info_bar.pack_forget()

    def update_cursor_info_bar(self, event=None):
        row, col = self.content_text.index(tk.INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        self.cursor_info_bar.config(text=infotext)


    def change_theme(self, event=None):
        selected_theme = self.theme_choice.get()
        fg_bg_colors = self.color_schemes.get(selected_theme)
        foreground_color, background_color = fg_bg_colors.split('.')
        self.content_text.config(
            background=background_color, fg=foreground_color)

    def update_line_numbers(self, event=None):
        line_numbers = self.get_line_numbers()
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete('1.0', 'end')
        self.line_number_bar.insert('1.0', line_numbers)
        self.line_number_bar.config(state='disabled')

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

    def on_content_changed(self, event=None):
        self.update_line_numbers()
        self.update_cursor_info_bar()

    def get_line_numbers(self):
        output = ''
        if self.show_line_number.get():
            row, col = self.content_text.index("end").split('.')
            for i in range(1, int(row)):
                output += str(i) + '\n'
        return output

    def display_about_messagebox(self, event=None):
        tk.messagebox.showinfo(
            "About", "{}{}".format(PROGRAM_NAME,
                            "\nText Editor GUI\nHackAnons\nhackanons@yahoo.com"))

    def display_help_messagebox(self, event=None):
        tk.messagebox.showinfo(
            "Help", "Help Book: \nText Editor GUI\nHackAnons\nhackanons@yahoo.com",
            icon='question')

    def exit_editor(self, event=None):
        if tk.messagebox.askokcancel("Quit?",
            "Do you want to QUIT for sure?\n Make sure you've saved your current work."):
            # root.destroy()
            self.parent.master.destroy()

    def new_file(self, event=None):
        self.parent.master.title("Untitled")
        global file_name
        file_name = None
        self.content_text.delete(1.0, tk.END)
        self.on_content_changed()

    def open_file(self, event=None):
        input_file_name = tk.filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            self.parent.master.title('{} - {}'.format(
                os.path.basename(file_name), PROGRAM_NAME))
            self.content_text.delete(1.0, tk.END)
            with open(file_name) as _file:
                self.content_text.insert(1.0, _file.read())

            self.on_content_changed()


    def write_to_file(self, file_name):
        try:
            content = self.content_text.get(1.0, 'end')
            with open(file_name, 'w') as the_file:
                the_file.write(content)
        except IOError:
            tk.messagebox.showwarning("Save", "Could not save the file.")

    def save_as(self, event=None):
        input_file_name = tk.filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                ("Text Documents", "*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            self.write_to_file(file_name)
            root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        return "break"

    def save(self, event=None):
        global file_name
        if not file_name:
            self.save_as()
        else:
            self.write_to_file(file_name)
        return "break"

    def select_all(self, event=None):
        self.content_text.tag_add('sel', '1.0', 'end')
        return "break"

    def find_text(self, event=None):
        search_toplevel = tk.Toplevel(self.parent.master)
        search_toplevel.title('Find Text')
        search_toplevel.transient(self.parent.master)

        tk.Label(search_toplevel, text="Find All:").grid(row=0, column=0,
                                                      sticky='e')

        search_entry_widget = tk.Entry(
            search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        ignore_case_value = tk.IntVar()
        tk.Checkbutton(search_toplevel, text='Ignore Case',
                    variable=ignore_case_value).grid(
                    row=1, column=1, sticky='e', padx=2, pady=2)
        tk.Button(search_toplevel, text="Find All", underline=0,
               command=lambda: self.search_output(
                   search_entry_widget.get(), ignore_case_value.get(),
                   self.content_text, search_toplevel, search_entry_widget)
               ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window(self):
        self.content_text.tag_remove('match', '1.0', tk.END)
        search_toplevel.destroy()
        search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
        return "break"


    def search_output(self, needle, if_ignore_case, content_text,
                      search_toplevel, search_box):
        content_text.tag_remove('match', '1.0', tk.END)
        matches_found = 0
        if needle:
            start_pos = '1.0'
            while True:
                start_pos = content_text.search(needle, start_pos,
                                                nocase=if_ignore_case, stopindex=tk.END)
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


    def cut(self):
        self.content_text.event_generate("<<Cut>>")
        self.on_content_changed()
        return "break"

    def copy(self):
        self.content_text.event_generate("<<Copy>>")
        return "break"

    def paste(self):
        self.content_text.event_generate("<<Paste>>")
        self.on_content_changed()
        return "break"

    def undo(self):
        self.content_text.event_generate("<<Undo>>")
        self.on_content_changed()
        return "break"

    def redo(self, event=None):
        self.content_text.event_generate("<<Redo>>")
        self.on_content_changed()
        return 'break'


def main():
    root = tk.Tk()
    root.geometry("800x600")
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
