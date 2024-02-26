from tkinter import Tk, Label, Button, filedialog, ttk
from cryptography.fernet import Fernet
import cv2
import glob
import os

def generate_key():
    return Fernet.generate_key()

# Save key to a file
def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    if not os.path.exists(filename):
        key = generate_key()
        save_key(key, filename)
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_image(filename, key):
    with open(filename, 'rb+') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def decrypt_image(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def get_files():
    files = glob.glob('*.sec')
    if len(files) > 0:
        output['values'] = files
        output.current(0)

def encrypt():
    filename = filedialog.askopenfilename(title='Select pic to encrypt')
    key = load_key('key.key')
    encrypted_data = encrypt_image(filename, key)
    name = filename.split('/')[-1].split('.')[0] + '.sec'
    with open(name, 'wb') as f:
        f.write(encrypted_data)
    os.remove(filename)

def decrypt():
    name = output.get()
    key = load_key('key.key')
    with open(name, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_image(encrypted_data, key)
    name = name.split('.')[0] + '.png'
    with open(name, 'wb') as f:
        f.write(decrypted_data)
    os.remove(output.get())

window = Tk()
window.title('Image Encryptor')
window.geometry('400x500')

Label(window, text="Image Encryptor", font=("Candara", 14)).pack(pady=4)

output = ttk.Combobox(window)
files = get_files()
output.pack()

Button(window, text="Encrypt", command=encrypt).pack(pady=20)
Button(window, text="Decrypt", command=decrypt).pack(pady=20)

window.mainloop()
