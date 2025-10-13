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


window = Tk()
window.geometry("500x500")

greeting = Label(text="Hello, inte",width="0", height="0")
greeting.pack()

label = Label(
    text="Hello, inte",
    fg="white",
    bg="black",
    width=10,
    height=5
)
label.pack()

button = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="gray",
    fg="black"
)
button.pack()
name = Label(text="Name")
nameIP = Entry()
name.pack()
nameIP.pack()

window.mainloop()
