from tkinter import *

def leftClickButton(event):
    calW = int(textboxW.get())
    calH = int(textboxH.get())/100
    print(f'{calW//(calH**2)}')
    #ยกกำลัง2 สามารถ import math มาใช้ math.pow(ตัวแปร,2) ได้เช่นเดียวกัน
    LabelCal.configure(text=calW//(calH**2))

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
#ให้สิ่งที่คำนวณไปโชว์บน GUI ไม่ใช่ในหน้าRunของpycharm
LabelCal = Label(Mainwindow,text="ผลลัพธ์")
LabelCal.grid(row=2,column=1)
Mainwindow.mainloop()