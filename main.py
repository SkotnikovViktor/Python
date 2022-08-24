a = 0
def click():
    global a
    a += 1
    print(a)


# Импорт библиотеки
import tkinter as tk
root = tk.Tk()
root.title("Программа для кликанья")
btn = tk.Button(root,text = "Кликни на мне срочно", command=click)
btn.pack()
root.geometry("500x500")
root.mainloop()
