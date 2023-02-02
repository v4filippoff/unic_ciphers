import tkinter as tk
from tkinter import messagebox

from src.logic import rsa_cipher
from src.logic.dto import RSAPublicKey, RSAPrivateKey
from src.logic.exceptions import TooBigMessage


def build_window():
    MIN_ALLOWED_BITS = 256

    def showerror_incorrect_key_length() -> None:
        messagebox.showerror(title='Ошибка', message='Минимальная битность 256')

    def showerror_incorrect_key() -> None:
        messagebox.showerror(title='Ошибка', message='Введите корректную битность')

    def showerror_source_text() -> None:
        messagebox.showerror(title='Ошибка', message='Введите корректно исходный текст')

    def showerror_encrypted_text() -> None:
        messagebox.showerror(title='Ошибка', message='Введите корректно зашифрованный текст')

    def showerror_custom(text: str) -> None:
        messagebox.showerror(title='Ошибка', message=text)

    def set_entry_text(entry: tk.Entry, text: str, disable_after: bool = True) -> None:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.insert(0, text)
        entry.config(state=(tk.DISABLED if disable_after else tk.NORMAL))

    def generate_keys():
        try:
            nbits: int = int(bits_input.get().strip().replace('-', '!'))
        except ValueError:
            showerror_incorrect_key()
            return
        if nbits < MIN_ALLOWED_BITS:
            showerror_incorrect_key_length()
            return

        key_generation = rsa_cipher.generate_keys(nbits)
        set_entry_text(p_input, str(key_generation.p))
        set_entry_text(q_input, str(key_generation.q))
        set_entry_text(euler_input, str(key_generation.euler))
        set_entry_text(n_input, str(key_generation.public_key.n))
        set_entry_text(e_input, str(key_generation.public_key.e))
        set_entry_text(d_input, str(key_generation.private_key.d))

    def encrypt_command():
        public_key = RSAPublicKey(e=int(e_input.get()), n=int(n_input.get()))
        source_text = source_text_input.get(1.0, tk.END).strip()
        if not source_text:
            showerror_source_text()
            return
        try:
            encrypted_text = rsa_cipher.encrypt(source_text, public_key)
        except TooBigMessage as exc:
            showerror_custom(str(exc))
            return
        encrypt_result_input.delete(1.0, tk.END)
        encrypt_result_input.insert(tk.END, str(encrypted_text))

    def decrypt_command():
        private_key = RSAPrivateKey(d=int(d_input.get()), n=int(n_input.get()))
        encrypted_text = encrypt_result_input.get(1.0, tk.END).strip()
        if not encrypted_text:
            showerror_encrypted_text()
            return
        try:
            decrypted_text = rsa_cipher.decrypt(int(encrypted_text), private_key)
        except TooBigMessage as exc:
            showerror_custom(str(exc))
            return
        decrypt_result_input.delete(1.0, tk.END)
        decrypt_result_input.insert(tk.END, decrypted_text)

    window = tk.Tk()
    window.geometry('1000x800')
    window.title('RSA Cipher')

    source_text_frame = tk.Frame(window)
    source_text_frame.grid(row=0, column=0)
    source_text_label = tk.Label(source_text_frame, text='Исходный текст')
    source_text_label.grid(row=0, column=0)
    source_text_input = tk.Text(source_text_frame, width=60, height=20)
    source_text_input.grid(row=1, column=0)

    params_frame = tk.Frame(window)
    params_frame.grid(row=0, column=1)

    bits_label = tk.Label(params_frame, text='bits')
    bits_label.grid(row=0, column=0)
    bits_input = tk.Entry(params_frame)
    bits_input.grid(row=0, column=1)

    p_label = tk.Label(params_frame, text='p')
    p_label.grid(row=1, column=0)
    p_input = tk.Entry(params_frame)
    p_input.config(state=tk.DISABLED)
    p_input.grid(row=1, column=1)

    q_label = tk.Label(params_frame, text='q')
    q_label.grid(row=2, column=0)
    q_input = tk.Entry(params_frame)
    q_input.config(state=tk.DISABLED)
    q_input.grid(row=2, column=1)

    euler_label = tk.Label(params_frame, text='euler')
    euler_label.grid(row=3, column=0)
    euler_input = tk.Entry(params_frame)
    euler_input.config(state=tk.DISABLED)
    euler_input.grid(row=3, column=1)

    n_label = tk.Label(params_frame, text='n')
    n_label.grid(row=4, column=0)
    n_input = tk.Entry(params_frame)
    n_input.config(state=tk.DISABLED)
    n_input.grid(row=4, column=1)

    e_label = tk.Label(params_frame, text='e')
    e_label.grid(row=5, column=0)
    e_input = tk.Entry(params_frame)
    e_input.config(state=tk.DISABLED)
    e_input.grid(row=5, column=1)

    d_label = tk.Label(params_frame, text='d')
    d_label.grid(row=6, column=0)
    d_input = tk.Entry(params_frame)
    d_input.config(state=tk.DISABLED)
    d_input.grid(row=6, column=1)

    generate_keys_button = tk.Button(params_frame, text='Сгенерировать', command=generate_keys)
    generate_keys_button.grid(row=7, column=1)

    encrypt_frame = tk.Frame(window)
    encrypt_frame.grid(row=3, column=0)
    encrypt_button = tk.Button(encrypt_frame, text='Зашифровать', command=encrypt_command)
    encrypt_button.grid(row=0, column=0)
    encrypt_result_input = tk.Text(encrypt_frame, width=60, height=20)
    encrypt_result_input.grid(row=1, column=0)

    decrypt_frame = tk.Frame(window)
    decrypt_frame.grid(row=3, column=1)
    decrypt_button = tk.Button(decrypt_frame, text='Расшифровать', command=decrypt_command)
    decrypt_button.grid(row=0, column=0)
    decrypt_result_input = tk.Text(decrypt_frame, width=60, height=20)
    decrypt_result_input.grid(row=1, column=0)

    window.mainloop()


if __name__ == '__main__':
    build_window()
