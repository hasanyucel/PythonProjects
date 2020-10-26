import win32gui, win32con
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
from tkinter import * 
from tkinter import ttk
import random,string

def generate():
    password.set(''.join(random.choices(data,k = int(n.get()))))

window = Tk()              # Create instance 
window.title("Şifre Oluşturucu") 
n = StringVar()
password = StringVar()
data = '!@#$%&*' + string.ascii_letters + string.digits

ttk.Label(window, text = "Uzunluk :", ).grid(
   column = 0, row = 0, pady = 10)

combo = ttk.Combobox(window, width = 4, textvariable = n)
combo['values'] = [i for i in range(6,21)]
combo.grid(column = 1, row = 0, pady = 10)

ttk.Button(window,text = "Oluştur",command = generate).grid(
    row = 0, column = 2,pady = 10,padx = 5)
ttk.Entry(window,textvariable = password).grid(
    row = 0, column = 3,pady = 10,padx = 5)

window.mainloop()