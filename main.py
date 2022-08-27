
import tkinter as tk

a = 0
def click():
    global a
    a += 1
    

def end():
    txt = tk.Label(text = f"Всего кликов {a}")
    txt.pack()
    return txt





root = tk.Tk()
root.title("Программа для кликанья")
root.geometry("500x500")




btn = tk.Button(root,text = "Кликни на мне срочно", command=click)
btn.pack()

btn2 = tk.Button(root,text = "Посчитаить сколько всего кликов", command = end)
btn2.pack()


root.mainloop()
