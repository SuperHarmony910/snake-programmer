# Credits to Data to Fish: https://datatofish.com/entry-box-tkinter/, RealPython: https://realpython.com/python-gui-tkinter/, https://realpython.com/run-python-scripts
#TODO More functionality, an epilogue and more goddamn style tbh.

import tkinter as tk

master = tk.Tk()

master.title("Greetings!")

canvas1 = tk.Canvas(master, width = 400, height = 300)
canvas1.pack()

# Canvas creation
heading = tk.Label(master, text='Greetings!')
heading.config(font=('helvetica', 14)) 
canvas1.create_window(200, 25, window=heading)

canvas2 = tk.Canvas(master, width = 400, height = 100)
canvas2.pack()

# Adding to structures

entry1 = tk.Entry(master) 
entry1.insert(0, '<enter-name>')
test = tk.Label(master, text="test")

canvas1.create_window(200, 145, window=entry1)
   
# Functions start
def greeting ():
    name = entry1.get()
    greet_me = tk.Label(master, text='Hello ' + name + '!', fg='lime', font=('monospace', 14, 'bold'))
    greet_me.config(font=('monospace', 12, 'bold'))
    canvas1.create_window(200, 260, window=greet_me)
    canvas2.create_window(400, 325, window=test)
    
button1 = tk.Button(text='Greetings!', command=greeting, bg='red', fg='white')
canvas1.create_window(200, 200, window=button1)


master.mainloop()
