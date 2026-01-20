from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("Nelze")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def key_input(event):
    if event.char in "0123456789+-*/.":
        button_press(event.char)

def key_enter(event):
    equals()

def key_backspace(event):
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

window = Tk()
window.title("Kalkulačka")
window.geometry("450x533")
window.resizable(False,False)
window.configure(bg="#1e1e1e")

equation_text = ""
equation_label = StringVar()

label = Label(
    window,
    textvariable=equation_label,
    font=('Segoe UI', 22),
    bg="#111",
    fg="white",
    width=24,
    height=2,
    anchor="e"
)
label.pack(pady=10)

frame = Frame(window, bg="#1e1e1e")
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(1))
button2 = Button(frame, text=2, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(2))
button3 = Button(frame, text=3, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(3))
button4 = Button(frame, text=4, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(4))
button5 = Button(frame, text=5, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(5))
button6 = Button(frame, text=6, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(6))
button7 = Button(frame, text=7, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(7))
button8 = Button(frame, text=8, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(8))
button9 = Button(frame, text=9, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(9))
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press(0))

plus = Button(frame, text='+', height=4, width=9, font=35,
              bg="#3a3a3a", fg="white",
              command=lambda: button_press('+'))
minus = Button(frame, text='-', height=4, width=9, font=35,
               bg="#3a3a3a", fg="white",
               command=lambda: button_press('-'))
nasobek = Button(frame, text='*', height=4, width=9, font=35,
                  bg="#3a3a3a", fg="white",
                  command=lambda: button_press('*'))
deleno = Button(frame, text='/', height=4, width=9, font=35,
                bg="#3a3a3a", fg="white",
                command=lambda: button_press('/'))

rovna_se = Button(frame, text='=', height=4, width=9, font=35,
               bg="#4caf50", fg="white",
               command=equals)
tecka = Button(frame, text='.', height=4, width=9, font=35,
                 bg="#2d2d2d", fg="white",
                 command=lambda: button_press('.'))

vymazat = Button(frame, text='AC', height=4, font=35,
                 bg="#b33a3a", fg="white",
                 command=clear)

button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=0, column=2)
plus.grid(row=0, column=3)


button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
minus.grid(row=1, column=3)


button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
nasobek.grid(row=2, column=3)

button0.grid(row=3, column=0)
tecka.grid(row=3, column=1)
rovna_se.grid(row=3, column=2)
deleno.grid(row=3, column=3)

vymazat.grid(row=4, column=0, columnspan=4, sticky="ew")

window.bind("<Key>", key_input)
window.bind("<Return>", key_enter)
window.bind("<BackSpace>", key_backspace)
window.bind("<Escape>", lambda e: clear())

window.mainloop()
