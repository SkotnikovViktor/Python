a = 0
b = True
def click():
    global a
    a += 1
    print(a)
    if a == 5:
        print("5!!!")

import tkinter as tk
root = tk.Tk()
root.title("Программа для кликанья")
btn = tk.Button(root,text = "Кликни на мне срочно", command=click)

root.geometry("500x500")
btn.pack()
root.mainloop()
