# Credits to https://datatofish.com/entry-box-tkinter/ & https://realpython.com/python-gui-tkinter/

import tkinter as tk
master = Tk()
window = tk.Tk()
entry = tk.Entry(root)
name = entry.get

greeting_str = tk.Label(text="Hello " + name + "!")
def greeting():
 greeting_str.pack()
 window.mainloop()

button1 = tk.Button(text="Click me once you've typed your name! ", command=greeting)
button1.pack

