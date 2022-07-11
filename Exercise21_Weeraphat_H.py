#BMI CAL
from tkinter import *
def leftClickButton(event):
    #print(float(textBoxWeight.get()) / (float(textBoxHeight.get()) / 100)**2)
    #labelResult.configure(text=float(textBoxWeight.get()) / (float(textBoxHeight.get()) / 100)**2)
    BMI = float(textBoxWeight.get()) / ((float(textBoxHeight.get()) / 100)**2)
    labelResult.configure(text = BMI)
    if BMI > 30:
        labelResult2.configure(text ="อ้วนมาก / โรคอ้วนระดับ 3")
    elif BMI >= 25 :
        labelResult2.configure(text ="อ้วน / โรคอ้วนระดับ 2")
    elif BMI >= 23 :
        labelResult2.configure(text ="ท้วม / โรคอ้วนระดับ 1")
    elif BMI >= 18.5 :
        labelResult2.configure(text="ปกติ (สุขภาพดี)")
    elif BMI < 18.5:
        labelResult2.configure(text="น้ำหนักน้อย / ผอม")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2)
labelResult2 = Label(MainWindow,text="Result")
labelResult2.grid(row=3,column=1)
labelResult = Label(MainWindow,text="BMI")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()