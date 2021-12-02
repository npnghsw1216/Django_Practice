from tkinter import *
from functools import partial
from tkinter import messagebox
import tkinter as tk

window=tk.Tk()
window.title("BMI Calculator")

def bmi(label_result, ht, wt):
    ht = float((ht.get()))
    wt = float((wt.get()))
    ht=ht/100
    bmi=float(wt / (ht*ht))
    bmi=round(bmi,1)

    conclusion=""

    if bmi < 18.5:
        messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 저체중 입니다. BMI : {bmi}')
    elif (bmi > 18.5) and (bmi < 23):
        messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 정상 입니다. BMI : {bmi}')
    elif (bmi > 23) and (bmi < 25):
        messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 과체중 입니다. BMI : {bmi}')
    elif (bmi > 25) and (bmi < 30):
        messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 비만 입니다. BMI :  {bmi}')
    elif bmi > 30:
        messagebox.showinfo('bmi-calculate', f'당신의 BMI 수치는 고도비만 입니다. BMI :  {bmi}')
    else:
        messagebox.showerror('bmi-calculate', '잘못됬습니다!')

    output= "BMI = "+str(bmi)+"\n" +conclusion

    label_result.config(text=output)
    return

ht = tk.StringVar()
wt = tk.StringVar()

heightText=Label(window,text="Height (in CM)").grid(row=0, padx=10,pady=10)
height=Entry(window, textvariable = ht ).grid(row=0, column=1, padx=10,pady=10)

weightText=Label(window,text="Weight (in KG)").grid(row=1, padx=10,pady=5)
weight=Entry(window, textvariable = wt ).grid(row=1, column=1, padx=10,pady=5)

labelResult = tk.Label(window)
labelResult.grid(row=4, column=0)

bmi = partial(bmi, labelResult, ht, wt)
btn=Button(window,text="Calculate BMI",command = bmi).grid(row=2, column=1, padx=20,pady=5)

window.geometry("400x300+10+10")
window.mainloop()
