# Credits to https://datatofish.com/entry-box-tkinter/ & https://realpython.com/python-gui-tkinter/
# Current issues: entry.get dysfunctional, button in wrong pos!

import tkinter as tk
window = tk.Tk()
entry = tk.Entry 
result = entry.get
name = "null"
name == result
window.title("Greetings!") 

greet_me = tk.Label(window, text="Hello " + name + "!")

def greeting():
 greet_me.place(relx = 0.5, rely = 0.5)

button1 = tk.Button(window, text="Click me once you've typed your name! ", command=greeting)
button1.place(height=50, width=400, relx = 0.5, rely = 0.5)

window.geometry("200x200") 
window.mainloop()
