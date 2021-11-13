import cv2
from tkinter import Tk,Label,Button,filedialog,ttk
import glob
import pickle
import os

def getFiles():

	files = glob.glob('*.sec')
	if len(files)>0:
		output['values'] = files
		output.current(0)


def Encrypt(): 
	filename = filedialog.askopenfilename(title = 'Select pic to encrypt')
	img = cv2.imread(filename)
	Name = filename.split('/')[-1].split('.')[0] + '.sec'

	f =  open(Name,'wb')

	pickle.dump(img,f)

	f.close()
	os.remove(filename)


def Decrypt(): 
	Name = output.get()
	f = open(Name,'rb')

	while True:
		try:
			e = pickle.load(f)
		except EOFError:
			break

	f.close()
	os.remove(Name)
	Name = Name.split('.')[0]

	cv2.imwrite(f'{Name}.png',e)



window = Tk()
window.title('Image Encryptor')
window.geometry('400x500')

Label(window,text = "Image Encryptor",font = ("Candara",14)).pack(pady=4)

output = ttk.Combobox(window)
files = getFiles()
output.pack()

Button(window,text = "Encrypt",command = Encrypt).pack(pady = 20)
Button(window,text = "Decrypt",command = Decrypt).pack(pady = 20)

window.mainloop()
