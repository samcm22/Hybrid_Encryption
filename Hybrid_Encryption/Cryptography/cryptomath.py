from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_key():
    return Fernet.generate_key()

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def perform_operation():
    operation = operation_var.get()
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    key = key_var.get().encode()

    if operation == 'encrypt':
        encrypt_file(input_file, output_file, key)
        messagebox.showinfo("Encryption", "File encrypted successfully!")
    elif operation == 'decrypt':
        decrypt_file(input_file, output_file, key)
        messagebox.showinfo("Decryption", "File decrypted successfully!")

def browse_file(entry_var):
    filename = filedialog.askopenfilename()
    entry_var.set(filename)

def main():
    global operation_var, input_file_var, output_file_var, key_var

    root = tk.Tk()
    root.title("File Encryption and Decryption Tool")

    operation_var = tk.StringVar(root, 'encrypt')
    input_file_var = tk.StringVar(root, '')
    output_file_var = tk.StringVar(root, '')
    key_var = tk.StringVar(root, '')

    tk.Label(root, text="Operation:").grid(row=0, column=0, sticky='w')
    tk.Radiobutton(root, text="Encrypt", variable=operation_var, value='encrypt').grid(row=0, column=1)
    tk.Radiobutton(root, text="Decrypt", variable=operation_var, value='decrypt').grid(row=0, column=2)

    tk.Label(root, text="Input File:").grid(row=1, column=0, sticky='w')
    tk.Entry(root, textvariable=input_file_var, width=50).grid(row=1, column=1, columnspan=2)
    tk.Button(root, text="Browse", command=lambda: browse_file(input_file_var)).grid(row=1, column=3)

    tk.Label(root, text="Output File:").grid(row=2, column=0, sticky='w')
    tk.Entry(root, textvariable=output_file_var, width=50).grid(row=2, column=1, columnspan=2)
    tk.Button(root, text="Browse", command=lambda: browse_file(output_file_var)).grid(row=2, column=3)

    tk.Label(root, text="Encryption Key:").grid(row=3, column=0, sticky='w')
    tk.Entry(root, textvariable=key_var, width=50).grid(row=3, column=1, columnspan=2)

    tk.Button(root, text="Perform Operation", command=perform_operation).grid(row=4, column=1, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
