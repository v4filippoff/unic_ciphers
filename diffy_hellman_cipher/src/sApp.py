import tkinter
from tkinter import *
from tkinter import messagebox
from s import gelfond_shanks



def btn_decide_click():
    try:
        int(number.get(1.0, END).strip())
        int(result.get(1.0, END).strip())
        int(mod_n.get(1.0, END).strip())
    except:
        messagebox.showerror('Error', 'Data is incorrect2')
        return
    numb = int(number.get(1.0, END))
    res = int(result.get(1.0, END))
    mod = int(mod_n.get(1.0, END))
    if numb > mod:
            messagebox.showerror('Error', 'Data is incorrect1')
            return
    exponent.delete(1.0, END)
    exponent.insert(1.0, str(gelfond_shanks(numb, mod, res)))




window = tkinter.Tk()
window.geometry('400x350')
window.title('task 1')
window['bg'] = '#9370db'
window.resizable(False, False)

number_label = Label(text='Число: ', background='#9370db')
number_label.place(x=20, y=50, width=50, height=20)
number = Text()
number.place(x=70, y=50, width=65, height=20)


exponent_label = Label(text='Степень: ', background='#9370db')
exponent_label.place(x=60, y=20, width=70, height=20)
exponent = Text()
exponent.place(x=130, y=20, width=65, height=20)


result_label = Label(text='A: ', background='#9370db')
result_label.place(x=60, y=120, width=70, height=20)
result = Text()
result.place(x=130, y=120, width=65, height=20)

mod_n_label = Label(text='mod: ', background='#9370db')
mod_n_label.place(x=130, y=50, width=50, height=20)
mod_n = Text()
mod_n.place(x=190, y=50, width=65, height=20)


btn_decide = Button(text='Решить', background='#9370db', command=btn_decide_click)
btn_decide.place(x=260, y=50, width=70, height=25)


if __name__ == "__main__":
    window.mainloop()