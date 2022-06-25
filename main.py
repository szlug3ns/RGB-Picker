import tkinter as tk
from tkinter import Tk, Text
import random

def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

r = random.randint(1, 255)
g = random.randint(1, 255)
b = random.randint(1, 255)

root = tk.Tk()
root.title('Random RGB Color Picker')
root.geometry('600x400+50+50')
root.resizable(False, False)
root.configure(bg=rgbtohex(r, g, b)) 

text = Text(root, height=5, bg=rgbtohex(r, g, b), bd=0, font=("Cascadia Mono", 16))
text.pack()

text.insert('1.0', str(r) + ', ' + str(g) + ', ' + str(b))

root.mainloop()