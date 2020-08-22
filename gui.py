# Credits to https://datatofish.com/entry-box-tkinter/ & https://realpython.com/python-gui-tkinter/

import tkinter as tk * from tkinter.ttk import *
window = tk.Tk()
entry = tk.Entry 
result = entry.get
name = "null"
name = result


greet_me = tk.Label(window, text="Hello " + name + "!")

def greeting():
 greet_me.pack()

button1 = tk.Button(window, text="Click me once you've typed your name! ", command=greeting)
button1.pack

master.geometry("200x200") 
window.mainloop()