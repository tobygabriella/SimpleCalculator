from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.config(bg="purple")
root.geometry('680x500+150+150')

e = Entry(root, width=50, borderwidth=5, bg="pink", fg="white",)
e.grid(row=0, column=0, columnspan=7, padx=20, pady=20)

button_text= ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue=1
columnvalue=0
for i in button_text:
    button= Button(root, text=i, width=8, height=4, command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue)
    columnvalue +=1
    if columnvalue>7:
        columnvalue =0
        rowvalue +=1



def click(value):
    v = e.get()
    answer = ''

    try:

        if value == 'C':
            v = v[0:len(v) - 1]  # 78
            e.delete(0, END)
            e.insert(0, v)
            return

        elif value == 'CE':
            e.delete(0, END)

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(v)))

        elif value == '√':
            answer = math.sqrt(eval(v))

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(v)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(v)))

        elif value == 'π':
            answer = math.pi

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'tanh':
            answer = math.tanh(eval(v))

        elif value == 'sinh':
            answer = math.sinh(eval(v))

        elif value == 'x\u02b8':
            e.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(v) ** 3

        elif value == 'x\u00B2':
            answer = eval(v) ** 2

        elif value == 'cosh':
            answer = math.cosh(eval(v))

        elif value == 'ln':
            answer = math.log2(eval(v))

        elif value == 'deg':
            answer = math.degrees(eval(v))

        elif value == "rad":
            answer = math.radians(eval(v))

        elif value == 'e':
            answer = math.e

        elif value == chr(8731):
            answer = eval(v) ** (1 / 3)

        elif value == 'log₁₀':
            answer = math.log10(eval(v))

        elif value == 'x!':
            answer = math.factorial(v)

        elif value == chr(247):  # 7/2=3.5
            e.insert(END, "/")
            return

        elif value == '=':
            answer = eval(v)

        else:
            e.insert(END, value)
            return

        e.delete(0, END)
        e.insert(0, answer)

    except SyntaxError:
        pass


root.mainloop()