import tkinter as tk
from tkinter import messagebox

from src.logic import xor_cipher


def build_window():

    def showerror_empty_key():
        messagebox.showerror(title='Ошибка', message='Ключ пустой!')

    def showerror_empty_source_text():
        messagebox.showerror(title='Ошибка', message='Исходный текст пустой!')

    def generate_random_key():
        source_text = source_text_input.get(1.0, tk.END)[:-1]
        if not source_text:
            showerror_empty_source_text()
            return
        key_text_input.delete(1.0, tk.END)
        key = xor_cipher.generate_random_key(len(source_text) * xor_cipher.BITS_IN_BYTE)
        bin_key_text_input.delete(1.0, tk.END)
        bin_key_text_input.insert(tk.END, key)

    def apply_xor():
        custom_key = key_text_input.get(1.0, tk.END)[:-1]
        bin_key = bin_key_text_input.get(1.0, tk.END)[:-1]
        if not custom_key and not bin_key:
            showerror_empty_key()
            return
        source_text = source_text_input.get(1.0, tk.END)[:-1]
        if not source_text:
            showerror_empty_source_text()
            return
        else:
            binary_source_text = xor_cipher.convert_str_to_binary_string(source_text)
            bin_source_text_input.delete(1.0, tk.END)
            bin_source_text_input.insert(tk.END, binary_source_text)

        if custom_key:
            bin_key = xor_cipher.convert_str_to_binary_string(xor_cipher.normalize_key(source_text, custom_key))
            bin_key_text_input.delete(1.0, tk.END)
            bin_key_text_input.insert(tk.END, bin_key)

        xor_result = xor_cipher.apply_xor(source_text, bin_key)
        crypto_text_input.delete(1.0, tk.END)
        crypto_text_input.insert(tk.END, xor_cipher.convert_binary_string_to_str(xor_result))
        bin_crypto_text_input.delete(1.0, tk.END)
        bin_crypto_text_input.insert(tk.END, xor_result)

    window = tk.Tk()
    window.geometry('1500x900')
    window.title('XOR Cipher')

    key_text_frame = tk.Frame(window)
    key_text_frame.grid(row=0, column=0)
    key_text_label = tk.Label(key_text_frame, text='Ключ')
    key_text_label.grid(row=0, column=0)
    key_text_input = tk.Text(key_text_frame, width=60, height=20)
    key_text_input.grid(row=1, column=0)

    source_text_frame = tk.Frame(window)
    source_text_frame.grid(row=0, column=1)
    source_text_label = tk.Label(source_text_frame, text='Исходный текст')
    source_text_label.grid(row=0, column=0)
    source_text_input = tk.Text(source_text_frame, width=60, height=20)
    source_text_input.grid(row=1, column=0)

    crypto_text_frame = tk.Frame(window)
    crypto_text_frame.grid(row=0, column=2)
    crypto_text_label = tk.Label(crypto_text_frame, text='Зашифрованный/Расшифрованный текст')
    crypto_text_label.grid(row=0, column=0)
    crypto_text_input = tk.Text(crypto_text_frame, width=60, height=20)
    crypto_text_input.grid(row=1, column=0)

    bin_key_text_frame = tk.Frame(window)
    bin_key_text_frame.grid(row=1, column=0)
    bin_key_text_label = tk.Label(bin_key_text_frame, text='Бинарный вид')
    bin_key_text_label.grid(row=0, column=0)
    bin_key_text_input = tk.Text(bin_key_text_frame, width=60, height=20)
    bin_key_text_input.grid(row=1, column=0)

    bin_source_text_frame = tk.Frame(window)
    bin_source_text_frame.grid(row=1, column=1)
    bin_source_text_label = tk.Label(bin_source_text_frame, text='Бинарный вид')
    bin_source_text_label.grid(row=0, column=0)
    bin_source_text_input = tk.Text(bin_source_text_frame, width=60, height=20)
    bin_source_text_input.grid(row=1, column=0)

    bin_crypto_text_frame = tk.Frame(window)
    bin_crypto_text_frame.grid(row=1, column=2)
    bin_crypto_text_label = tk.Label(bin_crypto_text_frame, text='Бинарный вид')
    bin_crypto_text_label.grid(row=0, column=0)
    bin_crypto_text_input = tk.Text(bin_crypto_text_frame, width=60, height=20)
    bin_crypto_text_input.grid(row=1, column=0)

    key_buttons_frame = tk.Frame(window)
    key_buttons_frame.grid(row=2, column=0)
    generate_key_button = tk.Button(key_buttons_frame, text='Сгенерировать ключ', command=generate_random_key)
    generate_key_button.grid(row=0, column=0)

    crypto_buttons_frame = tk.Frame(window)
    crypto_buttons_frame.grid(row=2, column=2)
    xor_button = tk.Button(crypto_buttons_frame, text='XOR', command=apply_xor)
    xor_button.grid(row=0, column=0)

    window.mainloop()


if __name__ == '__main__':
    build_window()
