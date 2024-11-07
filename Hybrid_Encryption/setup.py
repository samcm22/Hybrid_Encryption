from tkinter import *
from tkinter import ttk, messagebox
from Cryptography.hybrid_encryption import *
from getpass import getuser
from tkinter.filedialog import askopenfilename
from ttkthemes import themed_tk as tk


def message(name, button, mgs_label):
    """This function displays the message returned by either Encryption or Decryption."""
    button['state'] = DISABLED  # Disable the button after encryption or decryption
    if button["text"] == "Encryption":
        mgs = encryption(name)
        mgs_label.config(text=mgs)
    if button["text"] == "Decryption":
        mgs = decryption(name)
        mgs_label.config(text=mgs)


def open_file():
    """This function opens the file dialog box for choosing the file and creates encrypt and decrypt buttons."""
    username = getuser()
    initialdirectory = "C:/Users/{}".format(username)
    name = askopenfilename(initialdir=initialdirectory,
                           filetypes=[("All Files", "*.*")],
                           title="Choose a file."
                           )
    if name:
        file_name = get_file_name(name, extension=True)
        label.config(text=file_name)
        separator2 = ttk.Separator(root, orient='horizontal')
        separator2.place(relx=0, rely=0.38, relwidth=1, relheight=1)
        mgs_label = ttk.Label(root)
        mgs_label.place(x=0, y=150)
        encrypt_button = ttk.Button(root, text="Encryption", command=lambda: message(name, encrypt_button, mgs_label))
        decrypt_button = ttk.Button(root, text="Decryption", command=lambda: message(name, decrypt_button, mgs_label))
        encrypt_button.place(x=110, y=80)
        decrypt_button.place(x=210, y=80)


def about_page():
    """This function displays the 'About' page with information about the application."""
    about_window = Toplevel(root)  # Change this line to use Toplevel directly from tkinter
    about_window.title("About Hybrid Encryption")
    about_window.geometry("400x200")

    about_text = """
    Hybrid Encryption Application

    This application implements hybrid encryption, combining symmetric and asymmetric encryption algorithms.
    It provides a secure way to encrypt and decrypt files.

    Developed by sam@cm
    """

    about_label = ttk.Label(about_window, text=about_text, wraplength=380, justify="left")
    about_label.pack(padx=20, pady=20)


root = tk.ThemedTk()
root.get_themes()
root.set_theme("clearlooks")
icon = PhotoImage(file="images/icon.png")  # icon for the window
root.iconphoto(False, icon)
app_width = 600  # window width
app_height = 400  # window height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Evaluating X and Y coordinate such that, window always comes into the center.
x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))
root.geometry(f"{app_width}x{app_height}+{x}+{y}")
root.resizable(0, 0)  # Window size constant
title = root.title("Hybrid Encryption")
title_label = ttk.Label(root, text="Welcome to Hybrid Encryption Application", font=("Helvetica ", 16))
title_label.pack()
separator1 = ttk.Separator(root, orient='horizontal')
separator1.place(relx=0, rely=0.20, relwidth=1, relheight=1)
chose_file_button = ttk.Button(root, text="Choose File", command=open_file)
chose_file_button.pack()
label = ttk.Label(root, text="No chosen file")  # Label to display the name of selected file.
label.pack()

# Add an "About" button to the main window
about_button = ttk.Button(root, text="About", command=about_page)
about_button.pack()

root.mainloop()
