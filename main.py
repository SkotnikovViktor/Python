a = 0

def click():
    global a
    a += 1
    

def end():
    txt = tk.Label(text = a)
    txt.pack()
    return txt



import tkinter as tk

root = tk.Tk()
root.title("Программа для кликанья")


btn = tk.Button(root,text = "Кликни на мне срочно", command=click)
btn.pack()
btn2 = tk.Button(root,text = "Посчитаить сколько всего кликов", command = end)
btn2.pack()


root.geometry("500x500")
root.mainloop()
