from tkinter import *
from tkinter import ttk

'''
Widget Class	Description
Label	        A widget used to display text on the screen
Button	        A button that can contain text and can perform an action when clicked
Entry	        A text entry widget that allows only a single line of text
Text	        A text entry widget that allows multiline text entry
Frame	        A rectangular region used to group related widgets or provide padding between widgets
'''

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# count function
count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()
window.geometry("500x500")
window.title("tkinter basics")

icon = PhotoImage(file='logo.png') # converted png to photoImage
window.iconphoto(True, icon) # iconphoto() sets the icon of window
window.config(background='#101010')

greeting = Label(text="Hello, inte",width="0", height="0")
greeting.pack()

# pack() will just insert the label without coordinates

photo = PhotoImage(file='logo.png')

hello = Label(window,
    text="Hello, inte, do you even code??",
    font=('Arial', 20, 'italic'),
    fg="#ffffff",
    bg="#090909",
    relief='sunken',
    bd=10,
    padx=10,
    pady=10,
    image=photo,
    compound='bottom'
)
hello.pack()
# hello.place(x=100, y=100)



button = Button(window,
                command=click,
                text="Click me!",
                font=("comic sans", 10),
                fg='green',
                bg="gray",
                activeforeground='green',
                activebackground='gray',
                width=25,
                height=5,
                image=photo,
                compound='top'
)

button.pack()
name = Label(text="Name")
nameIP = Entry()
name.pack()
nameIP.pack()

# this will place window on computer screen, listen for events
window.mainloop()
