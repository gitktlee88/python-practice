from tkinter import *
### In case you are using Virtualenv on Windows I found a solution.
### I copied the "tcl" folder from C:\Python27\ over to
### the root of the Virtualenv.

# key down functionalitydef click():
def click():
    entered_text = textentry.get() # this'll collect the text from entry box
    output.delete(0.0, END) # clear the box
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry there was no word like " + entered_text
    output.insert(END, definition)

# exit function
def close_window():
    window.destroy()
    exit()



### main
window = Tk()
window.title("Tkinter practice")
#window.geometry("400x400")
window.configure(background="black")

### My Photo
photo1 = PhotoImage(file="cock.png")
Label (window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

#create Label
Label (window, text="Enter the word", bg="black", fg="white",
       font="noen 12 bold").grid(row=1, column=0, sticky=W)

#create a text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

#add a submit Button
Button (window, text="SUBMIT", width=6,
        command=click).grid(row=3, column=0, sticky=W)

#create another Label
Label (window, text="\nDefinition:", bg="black", fg="white",
       font="noen 12 bold").grid(row=4, column=0, sticky=W)

#create a text box
output = Text(window, width=75, height=6, wrap=WORD, bg="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#the dictionary
my_compdictionary = {
    'algorithm': 'Step by step instructions to complete a task',
    'bug': 'piece of code that causes errors'
}

#exit Label
Label (window, text="click to exit", bg="black", fg="white",
       font="noen 12 bold").grid(row=6, column=0, sticky=W)

#add an exit button
Button (window, text="Exit", width=14,
        command=close_window).grid(row=7, column=0, sticky=W)




### run main loop
window.mainloop()
