# Credits to Data to Fish: https://datatofish.com/entry-box-tkinter/, RealPython: https://realpython.com/python-gui-tkinter/, https://realpython.com/run-python-scripts
#TODO More functionality, an epilogue and more goddamn style tbh.

import tkinter as tk

master = tk.Tk()

master.title("Greetings!")
canvas1 = tk.Canvas(master, width = 400, height = 300)
canvas1.pack()

heading = tk.Label(master, text='Greetings!')
heading.config(font=('helvetica', 14)) 
canvas1.create_window(200, 25, window=heading)

canvas2 = tk.Canvas(master, width = 400, height = 100)
canvas2.pack()

entry1 = tk.Entry(master) 
canvas1.create_window(200, 145, window=entry1) 
    
def greeting ():
    name = entry1.get()
    greet_me = tk.Label(master, text='Hello ' + name + '!', fg='lime', font=('monospace', 12, 'bold'))
    greet_me.config(font=('monospace', 12, 'bold'))
    canvas1.create_window(200, 260, window=greet_me)
    
button1 = tk.Button(text='Greetings!', command=greeting, bg='red', fg='white')
canvas1.create_window(200, 200, window=button1)

master.mainloop()
