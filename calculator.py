from tkinter import *



window=Tk()

window.title("Calculator")
window.geometry("570x460")
window.configure(bg= "#1b1924")
window.resizable(False, False)
iconimage= PhotoImage(file="Screenshot from 2024-08-23 18-46-26.png")
window.iconphoto(True, iconimage)

equation = ""

def click2(event):
    global equation
    
    if(event.keysym=="BackSpace"):
        l=len(equation)
        equation=equation[0:l-1]
    elif(event.keysym=="KP_Multiply"):
        equation+="*"
    elif(event.keysym=="KP_Divide"):
        equation+="/"
    elif(event.keysym=="KP_Add"):
        equation+="+"
    elif(event.keysym=="KP_Subtract"):
        equation+="-"
    elif(event.keysym=="Return"):
        equation=str(eval(equation))
    elif(event.keysym=="Delete"):
        equation=""
    elif(event.keysym=="period"):
        equation+="."
    elif(event.keysym=="KP_Decimal"):
        equation+="."
    elif(event.keysym=="equal"):
        equation=str(eval(equation))
    else:
        equation +=event.keysym[3:]
    Label_result.config(text=equation)


def click(number):
    global equation
    equation += number
    Label_result.config(text=equation)
    
def clearall():
    global equation
    equation=""
    Label_result.config(text=equation)
    
def clear():
    global equation
    l=len(equation)
    equation=equation[0:l-1]
    Label_result.config(text=equation)
    
def calculation():
    global equation
    equation=str(eval(equation))
    Label_result.config(text=equation)
    
def percent():
    global equation
    equation= equation+"/100"
    equation=str(eval(equation))
    Label_result.config(text=equation)
    
    

Label_result= Label(window, width=30, height=2, text="", font=("comic sans", 24), bg="#44424e", fg="white")
Label_result.pack()

window.bind("<Key>", click2)

Button(window, width=5, height=1, text="AC", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2478b8", command=lambda: clearall()).place(x=13, y=100)
Button(window, width=5, height=1, text="C", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2478b8", command=lambda: clear()).place(x=150, y=100)
Button(window, width=5, height=1, text="/", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#1dbbdd", command=lambda: click("/")).place(x=290, y=100)
Button(window, width=5, height=1, text="+", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#1dbbdd", command=lambda: click("+")).place(x=430, y=100)

Button(window, width=5, height=1, text="7", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("7")).place(x=13, y=170)
Button(window, width=5, height=1, text="8", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("8")).place(x=150, y=170)
Button(window, width=5, height=1, text="9", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("9")).place(x=290, y=170)
Button(window, width=5, height=1, text="-", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#1dbbdd", command=lambda: click("-")).place(x=430, y=170)

Button(window, width=5, height=1, text="4", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("4")).place(x=13, y=240)
Button(window, width=5, height=1, text="5", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("5")).place(x=150, y=240)
Button(window, width=5, height=1, text="6", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("6")).place(x=290, y=240)
Button(window, width=5, height=1, text="x", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#1dbbdd", command=lambda: click("*")).place(x=430, y=240)

Button(window, width=5, height=1, text="1", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("1")).place(x=13, y=310)
Button(window, width=5, height=1, text="2", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("2")).place(x=150, y=310)
Button(window, width=5, height=1, text="3", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("3")).place(x=290, y=310)

Button(window, width=5, height=1, text="0", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click("0")).place(x=13, y=380)
Button(window, width=5, height=1, text=".", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: click(".")).place(x=150, y=380)
Button(window, width=5, height=1, text="%", font=("comic sans", 25, "bold"), bd=1, fg="white", bg="#2d2b37", command=lambda: percent()).place(x=290, y=380)

Button(window, width=6, height=3, text="=", font=("comic sans", 21, "bold"), bd=1, fg="white", bg="#042f5b", command=lambda: calculation()).place(x=430, y=310)



window.mainloop()
