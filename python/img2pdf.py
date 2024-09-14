import img2pdf
from PIL import Image

import os
import tkinter as tk
from tkinter import ttk
from tkinter import fd


file_types = (('jpeg files', '*.jpg'), ('png files', '*.png'), ('gif files', '*.gif'), ('pdf files', '*.pdf'), ('all files', '*.*'))

window = tk.Tk()
window.title = 'image to PDF file converter'
window.geometry('400x400')
window.resizable(False, False)
window.iconbitmap(os.path.join('.', 'img', 'favicon.ico'))

title_label = ttk.Label(text='image to PDF file converter')
title_label.grid(column=0, row=0, rowspan=2)

img_path = tk.StringVar(window, '')
img_path_entry = ttk.Entry(window, textvariable=file_path)
img_path_entry.grid(column=0, row=1)
def reconfirm_img_only_file_name():
    global img_only_file_name
    img_only_file_name = img_path.split(os.path.sep)[-1].replace('.jpg', '').replace('.png', '').replace('.gif', '')
reconfirm_img_only_file_name()

def browse_file_path_command():
    global img_path
    img_path.set(fd.askopenfilename(parent=window, title='select file', filetypes=file_types))
    print(file_path)
browse_img_path = ttk.Button(window, text='Browse', command=lambda: browse_file_path_command())
browse_img_path.grid(column=1, row=1)

def save_pdf_command():
    reconfirm_img_only_file_name()
    fd.asksaveasfile(filetypes=file_types, defaultextension=img_only_file_name+'.pdf')

'''
img_path = 'C:/Users/Admin/Desktop/GfG_images/do_nawab.png' # storing image path
pdf_path = 'C:/Users/Admin/Desktop/GfG_images/file.pdf' # storing pdf path
image = Image.open(img_path) # opening image
pdf_bytes = img2pdf.convert(image.filename) # converting into chunks using img2pdf
'''

'''only_file_name = image.filename.split(os.path.sep)[-1]'''

'''
file = open(pdf_path, 'wb') # opening or creating pdf file
file.write(pdf_bytes) # writing pdf files with chunks
image.close() # closing image file
file.close() # closing pdf file
print('Successfully made pdf file') # output
'''

window.mainloop()