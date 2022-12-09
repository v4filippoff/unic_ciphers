import tkinter as tk
from tkinter import messagebox, filedialog

from src.logic.breaking_vigenere_cipher import break_vigenere_cipher as break_cipher
from src.logic.exceptions import KeyLengthNotFound, NotOnlyAlphabetCharactersError


def build_window():

    def showerror_empty_input():
        messagebox.showerror(title='Ошибка', message='Введите исходный текст!')

    def showerror_two_alphabet_characters():
        messagebox.showerror(title='Ошибка', message='Символы текста должны быть из одного алфавита!')

    def showerror_key_length_not_found():
        messagebox.showerror(title='Ошибка', message='Не удалось найти длину ключа!')

    def showerror_not_only_alphabet_characters_error():
        messagebox.showerror(title='Ошибка', message='Допустимы только символы из алфавита!')

    def break_button_handler():
        source_text = source_text_input.get(1.0, tk.END)
        if len(source_text) == 1:
            showerror_empty_input()
            return

        try:
            break_cipher_result = break_cipher(source_text)
        except ValueError:
            showerror_two_alphabet_characters()
            return
        except KeyLengthNotFound:
            showerror_key_length_not_found()
            return
        except NotOnlyAlphabetCharactersError:
            showerror_not_only_alphabet_characters_error()
            return

        break_result_widget.delete(1.0, tk.END)
        break_result_widget.insert(tk.END, break_cipher_result.decrypted_text)
        key_input.delete(0, tk.END)
        key_input.insert(0, str(break_cipher_result.key))

    def select_file_button_handler():
        filetypes = [('Текстовые файлы', '*.txt')]

        filename = filedialog.askopenfilename(
            title='Открыть файл',
            initialdir='../',
            filetypes=filetypes
        )
        if not filename:
            return

        with open(filename, 'r') as file:
            source_text_input.delete(1.0, tk.END)
            source_text_input.insert(tk.END, file.read())

    window = tk.Tk()
    window.geometry('1000x800')
    window.title('Vigenere Cipher')

    source_text_frame = tk.Frame(window)
    source_text_frame.grid(row=0, column=0)
    source_text_label = tk.Label(source_text_frame, text='Исходный текст')
    source_text_label.grid(row=0, column=0)
    source_text_input = tk.Text(source_text_frame, width=60, height=20)
    source_text_input.grid(row=1, column=0)

    select_file_frame = tk.Frame(window)
    select_file_frame.grid(row=0, column=1)
    select_file_button = tk.Button(select_file_frame, text='Выбрать файл', command=select_file_button_handler)
    select_file_button.grid(row=1, column=0)

    break_frame = tk.Frame(window)
    break_frame.grid(row=3, column=0)
    break_button = tk.Button(break_frame, text='Взломать', command=break_button_handler)
    break_button.grid(row=0, column=0)
    break_result_widget = tk.Text(break_frame, width=60, height=20)
    break_result_widget.grid(row=1, column=0)

    key_frame = tk.Frame(window)
    key_frame.grid(row=3, column=1)
    key_label = tk.Label(key_frame, text='Ключ')
    key_label.grid(row=0, column=0)
    key_input = tk.Entry(key_frame)
    key_input.grid(row=1, column=0)

    window.mainloop()


if __name__ == '__main__':
    build_window()
