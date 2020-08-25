# Credits to Data to Fish: https://datatofish.com/entry-box-tkinter/, RealPython: https://realpython.com/python-gui-tkinter/, https://realpython.com/run-python-scripts
# Current issues: entry.get dysfunctional!

import tkinter as tk

master = tk.Tk()

master.title("Greetings!")
canvas1 = tk.Canvas(master, width = 400, height = 300)
canvas1.pack()

canvas2 = tk.Canvas(master, width = 400, height = 300)

entry1 = tk.Entry(master) 
canvas1.create_window(200, 145, window=entry1)

name = entry1.get()

greet_me = tk.Label(master, text = "Hello " + name + "!")
greet_me.config(font=('helvetica', 10))
    
def greeting ():
    canvas1.create_window(200, 230, window=greet_me)
    
button1 = tk.Button(text='Greetings!', command=greeting, bg='red', fg='white')
canvas1.create_window(200, 120, window=button1)

master.mainloop()
