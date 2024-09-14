import img2pdf
from PIL import Image

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as msgbox

file_types = (('image files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif', '*.png', '*.bmp', '*.jdib', '*.gif')), ('JPEG files', ('*.jpg', '*.jpeg', '*.jpe', '*.jfif')), ('PNG files', '*.png'), ('BMP files', ('*.bmp', '*.jdib')), ('GIF files', '*.gif'), ('PDF files', '*.pdf'), ('all files', '*.*'))

window = tk.Tk()
window.title = 'image to PDF file converter'
window.geometry('400x200')
window.resizable(False, False)
window.iconbitmap(os.path.join('.', 'img', 'favicon.ico'))

title_label = ttk.Label(text='image to PDF file converter')
title_label.grid(column=0, row=0, columnspan=2)

img_path_entry_stringvar = tk.StringVar(window, '')
img_path_entry = ttk.Entry(window, textvariable=img_path_entry_stringvar, width=40)
img_path_entry.grid(column=0, row=1)

def get_img_only_file_name(img_path):
    img_only_file_name = img_path.split(os.path.sep)[-1].replace('.jpg', '').replace('.png', '').replace('.gif', '')
    return img_only_file_name

def browse_img_path_command():
    global img_path, img_path_entry_stringvar
    img_path = fd.askopenfilenames(parent=window, title='select image file', filetypes=file_types)
    img_path_entry_stringvar_value = ''
    for i in img_path:
        img_path_entry_stringvar_value += i + '; '
    img_path_entry_stringvar.set(img_path_entry_stringvar_value)
    print(img_path)
    print(img_path_entry_stringvar.get())
browse_img_path = ttk.Button(window, text='Browse', command=lambda: browse_img_path_command())
browse_img_path.grid(column=1, row=1)

def convert_file_button_command(img_paths):
    for img_path in img_paths:
        img_only_file_name = get_img_only_file_name(img_path)
        image = Image.open(img_path)
        save_pdf_command(img_path)
convert_file_button = ttk.Button(window, text='convert file', command=lambda: convert_file_button_command(img_path))
convert_file_button.grid(column=1, row=2)

def save_pdf_command(img_path, img_only_file_name=None):
    if type(img_path) in (tuple, list):
        for i in img_path:
            save_pdf_command(i)
    if img_only_file_name is None: img_only_file_name = get_img_only_file_name(img_path)
    pdf_path = fd.asksaveasfilename(filetypes=file_types, defaultextension=img_only_file_name+'pdf')
    if pdf_path:
        try:
            with open(img_path, 'wb') as pdf_file:
                pdf_bytes = img2pdf.convert(image.filename)
                file.write(pdf_bytes)
                image.close()
            print('Successfully made pdf file')
        except Exception as e:
            result = msgbox.askretrycancel('Error Saving File!', 'Error Saving File! \nPlease Retry.')
            if result: window.after(100, convert_file_button_command, img_path, img_only_file_name)(filetypes=file_types, defaultextension=img_only_file_name+'.pdf')
save_pdf = ttk.Button(window, text='save PDF file', command=lambda: save_pdf_command(img_path_entry_stringvar.split('; ')))
save_pdf.grid(column=1, row=3)

window.mainloop()
