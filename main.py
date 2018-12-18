from tkinter import *

root=Tk()

root.title("Basic Calculator")
root.resizable(0,0)
root.wm_attributes("-topmost",1)

def btnPress(num):
    global equa
    equa=equa+str(num)
    equation.set(equa)

def equalPress():
    global equa
    total=str(eval(equa))
    equation.set(total)
    equa=""

def clearPress():
    global equa
    equa=""
    equation.set("")
    
equa=""
equation=StringVar()

calcLabel=Label(root,textvariable=equation,height=4)
equation.set("Enter your equation")
calcLabel.grid(columnspan=8)

button_0=Button(root,text="0",command=lambda:btnPress(0),padx=8,pady=8,height=3,width=6)
button_0.grid(row=4,column=1)
button_1=Button(root,text="1",command=lambda:btnPress(1),padx=8,pady=8,height=3,width=6)
button_1.grid(row=3,column=0)
button_2=Button(root,text="2",command=lambda:btnPress(2),padx=8,pady=8,height=3,width=6)
button_2.grid(row=3,column=1)
button_3=Button(root,text="3",command=lambda:btnPress(3),padx=8,pady=8,height=3,width=6)
button_3.grid(row=3,column=2)
button_4=Button(root,text="4",command=lambda:btnPress(4),padx=8,pady=8,height=3,width=6)
button_4.grid(row=2,column=0)
button_5=Button(root,text="5",command=lambda:btnPress(5),padx=8,pady=8,height=3,width=6)
button_5.grid(row=2,column=1)
button_6=Button(root,text="6",command=lambda:btnPress(6),padx=8,pady=8,height=3,width=6)
button_6.grid(row=2,column=2)
button_7=Button(root,text="7",command=lambda:btnPress(7),padx=8,pady=8,height=3,width=6)
button_7.grid(row=1,column=0)
button_8=Button(root,text="8",command=lambda:btnPress(8),padx=8,pady=8,height=3,width=6)
button_8.grid(row=1,column=1)
button_9=Button(root,text="9",command=lambda:btnPress(9),padx=8,pady=8,height=3,width=6)
button_9.grid(row=1,column=2)
button_plus=Button(root,text="+",command=lambda:btnPress("+"),padx=8,pady=8,height=3,width=6)
button_plus.grid(row=1,column=3)
button_minus=Button(root,text="-",command=lambda:btnPress("-"),padx=8,pady=8,height=3,width=6)
button_minus.grid(row=2,column=3)
button_multiply=Button(root,text="*",command=lambda:btnPress("*"),padx=8,pady=8,height=3,width=6)
button_multiply.grid(row=3,column=3)
button_divide=Button(root,text="/",command=lambda:btnPress("/"),padx=8,pady=8,height=3,width=6)
button_divide.grid(row=4,column=3)
button_equal=Button(root,text="=",command=equalPress,padx=8,pady=8,height=3,width=6)
button_equal.grid(row=4,column=2)
button_clear=Button(root,text="C",command=clearPress,padx=8,pady=8,height=3,width=6)
button_clear.grid(row=4,column=0)

root.mainloop()


