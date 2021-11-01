from cv2 import imread, imwrite
from pickle import load, dump
from tkinter import ttk,Tk,Label,Button,filedialog
from glob import glob
from os import remove


def getvalues():
	files = glob('*.secure')

	if len(files)>0:
		Files['values'] = files
		Files.current(0)


def space(times = 1):
	for i in range(times):
		Label(window,text = '').pack()

def encrypt():
	filetype = [('Images','*jpg')]

	filename = filedialog.askopenfilename(
		title = 'Open image to encrypt!',
		initialdir = './',
		filetypes = filetype
		)

	img = imread(filename)
	form = '.secure'

	Name = filename.split('/')[-1].split('.')[0]

	f = open(Name+form,'wb')
	dump(img,f)
	f.close()
	getvalues()
	remove(filename)

def decrypt():
	val = Files.get()

	Name = val.split('.')[0]
	f = open(val,'rb')

	while True:
		try:
			img = load(f)

		except EOFError: 
			break

	f.close()

	imwrite(f"{Name}.png",img)


window = Tk()
window.geometry('640x480')
window.resizable(False,False)

space()
Label(window, text = 'Image Encryptor',font =('Canadra',20)).pack()
space()

Files = ttk.Combobox(window)
Files.pack()
getvalues()

space(2)

Button(window,text = "Encrypt",font =('Canadra',14),command = encrypt).pack()
space(2)
Button(window,text = "Decrypt",font =('Canadra',14),command = decrypt).pack()
window.mainloop()