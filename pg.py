import os
from tkinter import Tk, Button

def button_click(button_number):
    file1 = "proj.py"
    file2 = "bmi.py"
    file3 = "simple.py"
    
    if button_number==1:
        os.system(f"python {file1}")

    elif button_number==2:
        os.system(f"python {file2}")

    elif button_number==3:
        os.system(f"python {file3}")



root = Tk()
root.title("Colored Buttons Example")
root.geometry("400x400")
root.resizable(0,0)
root.config(bg='#2e1907')


button1 = Button(root, text="AGE CALCULATOR", command=lambda: button_click(1), bg="#f5cba7")
button1.pack(pady=20)

button2 = Button(root, text="BMI CALCULATOR", command=lambda: button_click(2), bg="#f5cba7")
button2.pack(pady=20)

button3 = Button(root, text="ARITHMETIC CALCULATOR", command=lambda: button_click(3), bg="#f5cba7")
button3.pack(pady=20)


root.mainloop()
