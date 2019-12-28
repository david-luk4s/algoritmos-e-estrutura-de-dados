from tkinter import *

# instance Tk
window = Tk()

# set title
window.title('Hello World | Olá Mundo')

# add field
entry_text = Entry(window, width=100)
entry_text.pack()
entry_text.focus_set()

def call_back():
	print(entry_text.get())

btn = Button(window, text='Clique aqui', width=40, command=call_back)
btn.pack()

# size window
window.geometry('700x300')

# runig window
window.mainloop()
