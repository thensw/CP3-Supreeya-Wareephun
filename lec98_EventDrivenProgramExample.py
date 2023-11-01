from tkinter import *

def leftClickButton(event):
    print("left Click!")

def DoubleClickButton(event):
    print("Double Click!")

main = Tk()
button = Button(main,text="my button")
button.pack()
button.bind('<Button-1>', leftClickButton) # -1 คลิกเมาส์ซ้าย, -2 กดปุ่มเมาส์ตรงกลาง, -3 คลิกเมาส์ขวา
button.bind('<Double-1>', DoubleClickButton)
main.mainloop()