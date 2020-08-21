# Credits to https://datatofish.com/entry-box-tkinter/ & https://realpython.com/python-gui-tkinter/

import tkinter as tk
window = tk.Tk()
entry = tk.Entry 
name = entry.get

greeting = tk.Label(text="Hello " + name + "!")
def greeting():
 greeting.pack()
window.mainloop()

button1 = tk.Button(text="Click me once you've typed your name! ", command=greeting)

