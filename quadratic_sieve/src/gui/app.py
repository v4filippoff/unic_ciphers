import tkinter as tk
from tkinter import messagebox
from typing import Callable


def build_window():

    def showerror_empty_inputs():
        messagebox.showerror(title='Ошибка', message='Введите исходный текст и ключ!')

    window = tk.Tk()
    window.geometry('1000x800')
    window.title('Caesar Cipher')

    source_text_frame = tk.Frame(window)
    source_text_frame.grid(row=0, column=0)
    source_text_label = tk.Label(source_text_frame, text='Исходный текст')
    source_text_label.grid(row=0, column=0)
    source_text_input = tk.Text(source_text_frame, width=60, height=20)
    source_text_input.grid(row=1, column=0)

    select_language_frame = tk.Frame(window)
    select_language_frame.grid(row=0, column=1)
    select_language_label = tk.Label(select_language_frame, text='Выбрать язык')
    select_language_label.grid(row=0, column=0, columnspan=2)
    selected_language_variable = tk.StringVar()
    selected_language_variable.set('en')
    select_en_radiobutton = tk.Radiobutton(select_language_frame, text='EN', value='en', variable=selected_language_variable)
    select_ru_radiobutton = tk.Radiobutton(select_language_frame, text='RU', value='ru', variable=selected_language_variable)
    select_en_radiobutton.grid(row=1, column=0)
    select_ru_radiobutton.grid(row=1, column=1)

    key_frame = tk.Frame(window)
    key_frame.grid(row=2, column=0)
    key_label = tk.Label(key_frame, text='Ключ')
    key_label.grid(row=0, column=0)
    key_input = tk.Entry(key_frame)
    key_input.grid(row=1, column=0)

    encrypt_frame = tk.Frame(window)
    encrypt_frame.grid(row=3, column=0)
    encrypt_button = tk.Button(encrypt_frame, text='Зашифровать', command=lambda: None)
    encrypt_button.grid(row=0, column=0)
    encrypt_result_widget = tk.Text(encrypt_frame, width=60, height=20)
    encrypt_result_widget.grid(row=1, column=0)

    decrypt_frame = tk.Frame(window)
    decrypt_frame.grid(row=3, column=1)
    decrypt_button = tk.Button(decrypt_frame, text='Расшифровать', command=lambda: None)
    decrypt_button.grid(row=0, column=0)
    decrypt_result_widget = tk.Text(decrypt_frame, width=60, height=20)
    decrypt_result_widget.grid(row=1, column=0)

    window.mainloop()


if __name__ == '__main__':
    build_window()
