# Credits to https://datatofish.com/entry-box-tkinter/, https://realpython.com/python-gui-tkinter/, https://realpython.com/run-python-scripts
# Current issues: entry.get dysfunctional, button in wrong pos!

import tkinter as tk
master = tk.Tk()
entry = tk.Entry
canvas1.create_window(200, 140, window=entry)
entry.delete
result = entry.get
name = "null"
name == result
master.title("Greetings!") 

entry.pack

greet_me = tk.Label(window, text="Hello " + name + "!")

def greeting():
    name = entry.get
 greet_me.place(relx = 0.5, rely = 0.8)

button1 = tk.Button(window, text="Click me once you've typed your name! ", command=greeting)
button1.place(height=50, width=400, relx = 0.4, rely = 0.4)

master.geometry("200x200") 
mainloop()
