from tkinter import *

def leftClickButton(event):
    calW = int(textboxW.get())
    calH = int(textboxH.get())/100
    BMI = calW//(calH**2)
    print(BMI)
    if BMI>30:
        LabelCal.configure(text=f"อ้วนมาก")
    elif 25<BMI<29.9:
        LabelCal.configure(text="อ้วน")
    elif 23 < BMI < 24.9:
        LabelCal.configure(text="น้ำหนักเกิน")
    elif 18.6 < BMI < 22.9:
        LabelCal.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        LabelCal.configure(text="ผอมเกินไป")

Mainwindow = Tk()
LabelHeight = Label(Mainwindow,text="ส่วนสูง (cm.)")
LabelHeight.grid(row=0,column=0)
textboxH = Entry(Mainwindow)
textboxH.grid(row=0,column=1)
LabelWeight = Label(Mainwindow,text="น้ำหนัก (Kg.)")
LabelWeight.grid(row=1,column=0)
textboxW = Entry(Mainwindow)
textboxW.grid(row=1,column=1)
CalButton = Button(Mainwindow,text="คำนวณ")
CalButton.grid(row=2,column=0)
CalButton.bind('<Button-1>',leftClickButton)
LabelCal = Label(Mainwindow,text="ผลลัพธ์")
LabelCal.grid(row=2,column=1)
Mainwindow.mainloop()