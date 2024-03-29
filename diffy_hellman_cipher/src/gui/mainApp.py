import tkinter
from tkinter import *
from tkinter import messagebox
from src.logic.main import get_primitive_root, get_sg
import random


def build_window():
    def btn_decide_click():
        try:
            int(number.get(1.0, END))
            int(exponent.get(1.0, END))
            int(mod_n.get(1.0, END))
        except:
            messagebox.showerror('Error', 'Data is incorrect')
            return
        numb = int(number.get(1.0, END))
        exp = int(exponent.get(1.0, END))
        mod = int(mod_n.get(1.0, END))
        if numb > mod:
            messagebox.showerror('Error', 'Data is incorrect')
            return
        result.delete(1.0, END)
        result.insert(1.0, str(pow(numb, exp, mod)))

    def gen():
        try:
            a = int(number_bit.get(1.0, END).strip())
            b = int(mod_n_bit.get(1.0, END).strip())
            if a > b:
                messagebox.showerror('Error', 'Data is incorrect')
                return
        except:
            messagebox.showerror('Error', 'Data is incorrect')
            return
        number.delete(1.0, END)
        mod_n.delete(1.0, END)
        exponent.delete(1.0, END)
        p = get_sg(int(mod_n_bit.get(1.0, END).strip()) - 1) * 2 + 1
        number.insert(1.0, str(get_primitive_root(int(number_bit.get(1.0, END).strip()), p)))
        mod_n.insert(1.0, str(p))
        exponent.insert(1.0, str(random.randint(2, p - 1)))

    window = tkinter.Tk()
    window.geometry('400x350')
    window.title('task 1')
    window['bg'] = '#9370db'
    window.resizable(False, False)

    number_label = Label(text='g: ', background='#9370db')
    number_label.place(x=20, y=50, width=50, height=20)
    number = Text()
    number.place(x=70, y=50, width=65, height=20)

    number_label_bit = Label(text='bits: ', background='#9370db')
    number_label_bit.place(x=20, y=80, width=50, height=20)
    number_bit = Text()
    number_bit.place(x=70, y=80, width=65, height=20)

    exponent_label = Label(text='a: ', background='#9370db')
    exponent_label.place(x=60, y=20, width=70, height=20)
    exponent = Text()
    exponent.place(x=130, y=20, width=65, height=20)

    mod_n_label = Label(text='p: ', background='#9370db')
    mod_n_label.place(x=130, y=50, width=50, height=20)
    mod_n = Text()
    mod_n.place(x=190, y=50, width=65, height=20)

    mod_n_label_bit = Label(text='bits: ', background='#9370db')
    mod_n_label_bit.place(x=130, y=80, width=50, height=20)
    mod_n_bit = Text()
    mod_n_bit.place(x=190, y=80, width=65, height=20)

    btn_decide = Button(text='Решить', background='#9370db', command=btn_decide_click)
    btn_decide.place(x=260, y=50, width=70, height=25)

    btn_gen = Button(text='Gen', background='#9370db', command=gen)
    btn_gen.place(x=260, y=80, width=70, height=25)

    result_label = Label(text='Результат', background='#9370db')
    result_label.place()
    result = Text()
    result.place(x=0, y=200, width=400, height=150)

    window.mainloop()


if __name__ == "__main__":
    build_window()
