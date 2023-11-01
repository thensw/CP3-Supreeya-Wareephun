from tkinter import *

def sayHelloworld():
    print('Hello World')

mainWindow = Tk()
button = Button(mainWindow,text = "click me1",command = sayHelloworld,width=20).grid(row=0,column=1)
button2 = Button(mainWindow,text = "click me2",command = sayHelloworld).grid(row=1,column=2)

label = Label(mainWindow, text="Hello World", width=20,fg="red",bg="#FFCC00").grid(row=1,column=1)
mainWindow.mainloop()