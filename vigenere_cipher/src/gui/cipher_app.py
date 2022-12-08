import tkinter as tk
from tkinter import messagebox
from typing import Callable

from src.logic import vigenere_cipher
from src.logic.language_characters import check_language_identity


def build_window():

    def showerror_empty_inputs():
        messagebox.showerror(title='Ошибка', message='Введите исходный текст и ключ!')

    def showerror_incorrect_language_content():
        messagebox.showerror(title='Ошибка', message='Введите исходный текст и ключ в выбранном языке!')

    def showerror_incorrect_key():
        messagebox.showerror(title='Ошибка', message='Ключ может содержать только символы выбранного языка и цифры!')

    def encrypt_action(source_text, key, language_characters):
        encrypted_text = vigenere_cipher.encrypt(source_text, key, language_characters)
        encrypt_result_widget.delete(1.0, tk.END)
        encrypt_result_widget.insert(tk.END, encrypted_text)

    def decrypt_action(source_text, key, language_characters):
        decrypted_text = vigenere_cipher.decrypt(source_text, key, language_characters)
        decrypt_result_widget.delete(1.0, tk.END)
        decrypt_result_widget.insert(tk.END, decrypted_text)

    def cipher_action_button_handler(action_command: Callable):
        def returned_command():
            source_text = source_text_input.get(1.0, tk.END)
            key = key_input.get()

            if len(source_text) == 1 or not key:
                showerror_empty_inputs()
                return

            selected_language_value = selected_language_variable.get()
            if selected_language_value == 'en':
                language_characters = vigenere_cipher.LanguageCharacters.EN
            elif selected_language_value == 'ru':
                language_characters = vigenere_cipher.LanguageCharacters.RU

            if not check_language_identity(source_text, language_characters) or not \
                    check_language_identity(key, language_characters):
                showerror_incorrect_language_content()
                return

            if set(key) - set(vigenere_cipher.get_alphabet(language_characters)):
                showerror_incorrect_key()
                return

            return action_command(source_text, key, language_characters)

        return returned_command

    window = tk.Tk()
    window.geometry('1000x800')
    window.title('Vigenere Cipher')

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
    encrypt_button = tk.Button(encrypt_frame, text='Зашифровать', command=cipher_action_button_handler(encrypt_action))
    encrypt_button.grid(row=0, column=0)
    encrypt_result_widget = tk.Text(encrypt_frame, width=60, height=20)
    encrypt_result_widget.grid(row=1, column=0)

    decrypt_frame = tk.Frame(window)
    decrypt_frame.grid(row=3, column=1)
    decrypt_button = tk.Button(decrypt_frame, text='Расшифровать', command=cipher_action_button_handler(decrypt_action))
    decrypt_button.grid(row=0, column=0)
    decrypt_result_widget = tk.Text(decrypt_frame, width=60, height=20)
    decrypt_result_widget.grid(row=1, column=0)

    window.mainloop()


if __name__ == '__main__':
    build_window()
