# Hybrid_Encryption

This application is a graphical user interface (GUI) built with Tkinter to facilitate secure file encryption and decryption. It uses hybrid encryption techniques, combining symmetric and asymmetric encryption algorithms for secure data protection. The application allows users to select files for encryption and decryption, ensuring that sensitive data remains secure.

Features
File Selection: Users can select any file from their local system to encrypt or decrypt.
Hybrid Encryption: Utilizes a combination of symmetric and asymmetric encryption for optimal security.
User-Friendly Interface: A clean, intuitive interface for easy file selection, encryption, and decryption.
About Page: Provides details about the application's purpose and functionality.
File Encryption and Decryption Status: Displays messages indicating the status of the encryption or decryption process.
Prerequisites
Python 3.x
Tkinter: Comes pre-installed with Python.
ttkthemes: For enhanced Tkinter themes.
Cryptography Module: Custom module handling the encryption and decryption process.

# How to Run
Clone or Download the Repository: 
Run the Application:

# Usage
Start the Application.
Select a File by clicking "Choose File" to initiate encryption or decryption.
Click "Encryption" or "Decryption" to apply the desired operation on the selected file.
View the status message to confirm the operation's success.
Access the "About" page for information on the application.

# File Structure

HybridEncryptionApp/
├── images/
│   └── icon.png          # Application icon
├── main.py               # Main application code
├── Cryptography/
│   └── hybrid_encryption.py   # Encryption and decryption logic
└── README.md             # Project README

# Future Improvements
Additional encryption algorithms and techniques.
Enhanced file format compatibility.
Progress indicators for encryption and decryption processes.
