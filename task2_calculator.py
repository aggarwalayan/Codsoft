from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('Simple Calculator')
        master.geometry('360x260+0+0')
        master.config(bg='#2b2b2b')  # Adjusted background color
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=28, bg='#515151', font=('Noto Sans', 16), textvariable=self.equation, bd=8, insertwidth=2, justify="right", fg="white").place(x=0, y=0)  # Adjusted colors and font

        Button(width=8, text='(', relief='flat', command=lambda: self.show('('), bg="#444", fg="white").place(x=0, y=50)
        Button(width=8, text=')', relief='flat', command=lambda: self.show(')'), bg="#444", fg="white").place(x=90, y=50)
        Button(width=8, text='%', relief='flat', command=lambda: self.show('%'), bg="#444", fg="white").place(x=180, y=50)
        Button(width=8, text='1', relief='flat', command=lambda: self.show(1), bg="#444", fg="white").place(x=0, y=90)
        Button(width=8, text='2', relief='flat', command=lambda: self.show(2), bg="#444", fg="white").place(x=90, y=90)
        Button(width=8, text='3', relief='flat', command=lambda: self.show(3), bg="#444", fg="white").place(x=180, y=90)
        Button(width=8, text='4', relief='flat', command=lambda: self.show(4), bg="#444", fg="white").place(x=0, y=130)
        Button(width=8, text='5', relief='flat', command=lambda: self.show(5), bg="#444", fg="white").place(x=90, y=130)
        Button(width=8, text='6', relief='flat', command=lambda: self.show(6), bg="#444", fg="white").place(x=180, y=130)
        Button(width=8, text='7', relief='flat', command=lambda: self.show(7), bg="#444", fg="white").place(x=0, y=170)
        Button(width=8, text='8', relief='flat', command=lambda: self.show(8), bg="#444", fg="white").place(x=180, y=170)
        Button(width=8, text='9', relief='flat', command=lambda: self.show(9), bg="#444", fg="white").place(x=90, y=170)
        Button(width=8, text='0', relief='flat', command=lambda: self.show(0), bg="#444", fg="white").place(x=0, y=210)
        Button(width=8, text='.', relief='flat', command=lambda: self.show('.'), bg="#444", fg="white").place(x=90, y=210)
        Button(width=8, text='+', relief='flat', command=lambda: self.show('+'), bg="#444", fg="white").place(x=270, y=90)
        Button(width=8, text='-', relief='flat', command=lambda: self.show('-'), bg="#444", fg="white").place(x=270, y=130)
        Button(width=8, text='/', relief='flat', command=lambda: self.show('/'), bg="#444", fg="white").place(x=270, y=170)
        Button(width=8, text='x', relief='flat', command=lambda: self.show('*'), bg="#444", fg="white").place(x=270, y=210)
        Button(width=8, text='=', bg='green', relief='flat', command=self.solve, fg="white").place(x=180, y=210)
        Button(width=8, text='AC', relief='flat', command=self.clear, bg="#444", fg="white").place(x=270, y=50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()
