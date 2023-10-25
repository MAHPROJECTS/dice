print("helllllo humaira its mah")
print("mergeeeeeeeeeeeeeee")
print ("this better work")
import random


def generate_number():
    list = [ "1", "2", "3", "4", "5", "6"]
    number = ""
    for i in range(1):
        number = number + random.choice(list)
    l2.config(text=number)


import tkinter as tk

window = tk.Tk()
window.geometry("600x200")
window.config(bg="#1f77b4")
window.resizable(width=False, height=False)
window.title('Random Dice Number Generator')

l1 = tk.Label(text="Random Dice Number Generator", font=("Arial", 20), bg="Black", fg="White")

b1 = tk.Button(text="Click to roll the dice", font=("Arial", 15), bg="#1f77b4",
               command=generate_number)

l2 = tk.Label(bg="#1f77b4", font=("Arial", 30), text="")

l1.place(x=100, y=20)
b1.place(x=110, y=70)
l2.place(x=165, y=130)

window.mainloop()

print("hiii")
print("this is so annoying")
print("im literlaly crying cos this is so annoying like help")
